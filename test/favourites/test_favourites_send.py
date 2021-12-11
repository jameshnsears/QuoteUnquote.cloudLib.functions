from unittest.mock import Mock

from storage import favourites_adapter
from storage.unable_to_send_exception import UnableToSendException
from validation.request_validation_favourites import RequestValidationFavourites


def test_http_get_not_supported(client):
    assert client.get("/save").status_code == 405


def test_json_not_sent(client):
    response = client.post('/save')
    assert response.json['error'] == RequestValidationFavourites.RESPONSE_ERROR_JSON_NOT_VALID
    assert response.json['reason'] == RequestValidationFavourites.RESPONSE_REASON_NO_JSON
    assert response.status_code == 400


def test_empty_json(client):
    response = client.post('/save', json={})
    assert response.json['error'] == RequestValidationFavourites.RESPONSE_ERROR_JSON_NOT_VALID
    assert response.json['reason'] == RequestValidationFavourites.RESPONSE_REASON_EMPTY_JSON
    assert response.status_code == 400


def test_no_code(client):
    response = client.post('/save', json={'': ''})
    assert response.json['error'] == RequestValidationFavourites.RESPONSE_ERROR_JSON_NOT_VALID
    assert response.json['reason'] == RequestValidationFavourites.RESPONSE_REASON_NO_CODE
    assert response.status_code == 400


def test_code_length(client):
    response = client.post('/save', json={'code': ''})
    assert response.json['error'] == RequestValidationFavourites.RESPONSE_ERROR_JSON_NOT_VALID
    assert response.json['reason'] == RequestValidationFavourites.RESPONSE_REASON_LENGTH_CODE
    assert response.status_code == 400


def test_invalid_code(client):
    response = client.post('/save', json={'code': '0123456789'})
    assert response.json['error'] == RequestValidationFavourites.RESPONSE_ERROR_JSON_NOT_VALID
    assert response.json['reason'] == RequestValidationFavourites.RESPONSE_REASON_CRC_FAIL
    assert response.status_code == 400


def test_valid_code_but_missing_digests(client):
    response = client.post('/save', json={'code': "10000000d1"})
    assert response.json['error'] == RequestValidationFavourites.RESPONSE_ERROR_JSON_NOT_VALID
    assert response.json['reason'] == RequestValidationFavourites.RESPONSE_REASON_NO_DIGESTS
    assert response.status_code == 400


def test_valid_code_but_digests_length(client):
    response = client.post('/save', json={'code': "10000000d1", 'digests': []})
    assert response.json['error'] == RequestValidationFavourites.RESPONSE_ERROR_JSON_NOT_VALID
    assert response.json['reason'] == RequestValidationFavourites.RESPONSE_REASON_LENGTH_DIGESTS
    assert response.status_code == 400


def test_valid_request(client):
    response = client.post('/save',
                           json={
                               'code': "10000000d1",
                               'digests': ["01234567", "12345678"]})
    assert not response.is_json
    assert response.status_code == 200


def test_unable_to_send(client):
    favourites_adapter.favourites_send = Mock(side_effect=UnableToSendException())
    response = client.post('/save',
                           json={
                               'code': "10000000d1",
                               'digests': ["01234567", "12345678"]})
    assert response.json['error'] \
           == RequestValidationFavourites.RESPONSE_ERROR_UNABLE_TO_COMPLETE_SEND
    assert response.status_code == 400


def test_valid_send_request_against_schema(client):
    request_validation_favourites = RequestValidationFavourites()

    json = {
        "code": "10000000d1",
        "digests": [
            "01234567",
            "12345678"
        ]
    }
    assert request_validation_favourites.check_against_jsonschema(
        json, RequestValidationFavourites.JSONSCHEMA_FAVOURITES_SEND_REQUEST) is None
