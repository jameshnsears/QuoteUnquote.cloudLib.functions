import os
from flask import Flask, request

from endpoint.favourites import favourites_send, favourites_receive
from endpoint.transfer import transfer_backup, transfer_restore

app = Flask(__name__)


# called "Send" in the App
@app.route('/save', methods=['POST'])
def gcp_favourites_send():
    return favourites_send(request)


@app.route('/receive', methods=['POST'])
def gcp_favourites_receive():
    return favourites_receive(request)


@app.route('/transfer_backup', methods=['POST'])
def gcp_transfer_backup():
    return transfer_backup(request)


@app.route('/transfer_restore', methods=['POST'])
def gcp_transfer_restore():
    return transfer_restore(request)


# localhost HTTP into remote Firestore in GCP
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 8080)))
