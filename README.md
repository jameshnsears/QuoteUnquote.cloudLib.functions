# GCP Functions & (optional) Cloud Run

[![codecov](https://codecov.io/gh/jameshnsears/QuoteUnquote.cloudLib.functions/branch/main/graph/badge.svg?token=jc55AxH2ry)](https://codecov.io/gh/jameshnsears/QuoteUnquote.cloudLib.functions) [![deploy-gcp](https://github.com/jameshnsears/QuoteUnquote.cloudLib.functions/actions/workflows/deploy-gcp.yml/badge.svg)](https://github.com/jameshnsears/QuoteUnquote.cloudLib.functions/actions/workflows/deploy-gcp.yml)

NOTE: overlap between:

* <https://console.cloud.google.com/home/dashboard>
* <https://console.firebase.google.com>

## 1. Install GCP cli locally - Debian

```bash
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] \
    https://packages.cloud.google.com/apt cloud-sdk main" \
    | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

sudo apt install apt-transport-https ca-certificates gnupg

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg \
    | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

sudo apt update && sudo apt install google-cloud-sdk

gcloud init

# login via Web UI & create env - https://console.cloud.google.com/home/dashboard

# see config/*.gpg for env's

# use us_central1 - as it's part of free usage
```

---

## 2. In GCP dashboard

* create Project

### 2.1. Create Firestore instance

* Create Firestore
    * Native mode instance
    * eur3 (multi region)
    * favourites_collection
    * transfer_collection

### 2.2. Create Service Account

* create Service Account with roles:
    * Cloud Functions Admin
    * Firebase Admin SDK Administrator Service Agent
    * Service Account Token Creator
    * Service Account User
    * Logs Writer
* export JSON key of Service Account

## 3. In cli, for project, do one off tasks

```text
gcloud init

gcloud services enable cloudfunctions.googleapis.com

gcloud services enable cloudbuild.googleapis.com

gcloud services enable logging.googleapis.com
```

---

## 4. GitHub Secret - GOOGLE_APPLICATION_CREDENTIALS

* base64 config/dev-service-account.json

---

## 5. Test

Ensure venv created (as per GitHub workflows):

```text
/usr/bin/python3.11.2 -m venv --system-site-packages venv
source venv/bin/activate
pip install -r requirements-test.txt
pip install -r src/requirements.txt
```

### 5.1. pycharm

* extract config/*.gpg files
* run 'pytest gcp dev'

### 5.2. curl - localhost HTTP into remote Firestore in GCP

* NOTE: integration test, of remote functions HTTP, in GitHub workflow

run 'index gcp dev'

```text
export GOOGLE_APPLICATION_CREDENTIALS=config/dev-service-account.json

curl -v -X POST \
  http://127.0.0.1:8080/save \
  -H "Content-Type:application/json" \
  -d '{"code": "500000008b", "digests": ["01234567", "12345678"]}'
  
curl -v -X POST \
  http://127.0.0.1:8080/receive \
  -H "Content-Type:application/json" \
  -d '{"code": "500000008b"}'
  
curl -v -X POST \
  http://127.0.0.1:8080/transfer_backup \
  -H "Content-Type:application/json" \
  --data-binary "@test_data/transfer_backup_request.json"
  
curl -v -X POST \
  http://127.0.0.1:8080/transfer_restore \
  -H "Content-Type:application/json" \
  -d '{"code": "500000008b"}'  
```

---

## 6. (Optional) Cloud Run - using function src in docker container

* NOTE: azure has a similar container offering:
    * <https://docs.microsoft.com/en-us/azure/app-service/tutorial-custom-container?pivots=container-linux>
    * <https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-flask>
    * <https://azure.microsoft.com/en-gb/services/app-service/>

* Also uses, close to chargable, hard disk space in GCP

### 6.1. Build docker image (optional)

```text
docker images
docker rmi -f <id>
docker build --tag quoteunquote:latest .
docker run -it quoteunquote:latest sh
```

### 6.2. Test container locally (using remote Firestore)

```text
docker ps -a
docker rm <id>
docker run --rm -p 9090:8080 -e PORT=8080 -e \
    GOOGLE_APPLICATION_CREDENTIALS=dev-service-account.json \
    quoteunquote:latest

curl -v -X POST \
  http://127.0.0.1:9090/receive \
  -H "Content-Type:application/json" \
  -d '{"code": "500000008b"}'

docker stop <id>
docker rm <id>
```

### 6.3. Deploy to Cloud Run

* additional Service Account roles:
    * Cloud Run Admin
    * Cloud Run Service Agent

```text
docker images
docker tag <id> gcr.io/${GCP_PROJECT_ID_DEVELOPMENT}/quoteunquote:latest

docker push gcr.io/${GCP_PROJECT_ID_DEVELOPMENT}/quoteunquote:latest

gcloud run deploy quoteunquote --image gcr.io/${GCP_PROJECT_ID_DEVELOPMENT}/quoteunquote:latest \
  --platform managed --region=us-central1 --allow-unauthenticated \
  --set-env-vars=GOOGLE_APPLICATION_CREDENTIALS=/app/dev-service-account.json
```

#### 6.3.1. Integration Test

```text
curl -v -X POST \
  https://quoteunquote-<hashed id>-uc.a.run.app/receive \
  -H "Content-Type:application/json" \
  -d '{"code": "500000008b"}'

```

## 7. Deployment: Cloud Functions in GCP

* visit GCP instance in config/dev-service-account.json
    * <https://console.cloud.google.com/home/dashboard>
* see: deploy-gcp.yml

```text
cd src
cp ../config/dev-service-account.json .
gcloud functions delete save --quiet || true
gcloud functions deploy save --set-env-vars GOOGLE_APPLICATION_CREDENTIALS=dev-service-account.json --runtime python312 --trigger-http --allow-unauthenticated --gen2
```
