from datetime import datetime

from flask import jsonify
from google.cloud import firestore

from utils import logging_facade


def favourites_send(code, digests):
    logging_facade.info("favourites_send: " + "; ".join(digests))
    _get_collection_favourites().document(code).set(
        {'now': _get_utc_seconds(), 'digests': digests})


def favourites_retrieve(code):
    logging_facade.info("favourites_retrieve: " + code)
    document = _get_collection_favourites().document(code).get()
    if document.exists:
        return jsonify({'digests': document.to_dict()['digests']})
    return None


def transfer_backup(code, json):
    logging_facade.info("transfer_backup: " + "; ".join(json))

    json['now'] = _get_utc_seconds()

    _get_collection_transfer().document(code).set(json)


def transfer_restore(code):
    logging_facade.info("transfer_restore: " + code)
    document = _get_collection_transfer().document(code).get()
    if document.exists:
        return jsonify(
            {
                'transfer': document.to_dict(),
                'error': "",
                'reason': ""
            }
        )
    return None


def _get_collection_favourites():
    db = firestore.Client()
    return db.collection('favourites_collection')


def _get_collection_transfer():
    db = firestore.Client()
    return db.collection('transfer_collection')


def _get_utc_seconds():
    return (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()
