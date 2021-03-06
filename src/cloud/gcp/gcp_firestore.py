from datetime import datetime

from flask import jsonify
from google.cloud import firestore

from storage.unable_to_save_exception import UnableToSaveException
from utils import logging_facade


def save(code, digests):
    logging_facade.info("save: " + "; ".join(digests))

    try:
        _get_collection().document(code).set({'now': _get_utc_seconds(), 'digests': digests})
    except Exception as e:
        logging_facade.info(e)
        raise UnableToSaveException()


def retrieve(code):
    logging_facade.info("retrieve: " + code)

    document = _get_collection().document(code).get()
    if document.exists:
        return jsonify({'digests': document.to_dict()['digests']})

    return None


def _get_collection():
    db = firestore.Client()
    return db.collection('favourites_collection')


def _get_utc_seconds():
    return (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()
