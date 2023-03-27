from unittest import TestCase, mock

import flask
from flask import Flask
from endpoint.transfer import transfer_backup, transfer_restore


class TestMyApp(TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

    def test_transfer_backup_with_valid_request(self):
        with self.app.test_request_context('/backup', json={'data': 'backup_data'}):
            response = transfer_backup(flask.request)
            self.assertEqual(response.status_code, 200)

    def test_transfer_backup_with_invalid_request(self):
        with self.app.test_request_context('/backup', json={}):
            response = transfer_backup(flask.request)
            self.assertEqual(response.status_code, 400)

    @mock.patch('myapp.transfer_adapter.transfer_restore')
    def test_transfer_restore_with_valid_request(self, mock_restore):
        mock_restore.return_value = {'data': 'restore_data'}
        with self.app.test_request_context('/restore', json={'data': 'backup_data'}):
            response = transfer_restore(flask.request)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'data': 'restore_data'})

    def test_transfer_restore_with_invalid_request(self):
        with self.app.test_request_context('/restore', json={}):
            response = transfer_restore(flask.request)
            self.assertEqual(response.status_code, 400)
