import hashlib

from flask import jsonify
from jsonschema import validate, ValidationError


class RequestValidation:
    _JSONSCHEMA_REQUEST_RETRIEVE = {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "minLength": 10,
                "maxLength": 10
            },
        },
        "required": ["code"]
    }

    RESPONSE_ERROR_JSON_NOT_VALID = 'JSON not valid'
    RESPONSE_ERROR_UNABLE_TO_COMPLETE_SEND = 'unable to complete send'
    RESPONSE_REASON_CRC_FAIL = 'CRC fail'
    RESPONSE_REASON_EMPTY_JSON = 'empty JSON'
    RESPONSE_REASON_LENGTH_CODE = "'' is too short"
    RESPONSE_REASON_NO_CODE = 'no code'
    RESPONSE_REASON_NO_JSON = 'no JSON'
    RESPONSE_REASON_NO_JSON_FOR_CODE = 'no JSON for code'

    def _check_code(self, request):
        if not request.is_json:
            return self.report_error_with_request(self.RESPONSE_REASON_NO_JSON)

        if request.json == {}:
            return self.report_error_with_request(self.RESPONSE_REASON_EMPTY_JSON)

        if request.json.get('code', None) is None:
            return self.report_error_with_request(self.RESPONSE_REASON_NO_CODE)

        if len(request.json.get('code')) != 10:
            return self.report_error_with_request(self.RESPONSE_REASON_LENGTH_CODE)

        if not self._crc_check(request.json.get('code')):
            return self.report_error_with_request(self.RESPONSE_REASON_CRC_FAIL)

        return None

    @staticmethod
    def _crc_check(code):
        if code[8:] != hashlib.md5(code[:8].encode('utf-8')).hexdigest()[:2]:
            return False
        return True

    @staticmethod
    def check_against_jsonschema(json, schema):
        validate(instance=json, schema=schema)

    def check_request_receive(self, request):
        try:
            self.check_against_jsonschema(request.json, self._JSONSCHEMA_REQUEST_RETRIEVE)
        except ValidationError as e:
            return self.report_error_with_request(e.message)

        return self._check_code(request)

    def report_error_with_request(self, reason):
        return jsonify({'error': self.RESPONSE_ERROR_JSON_NOT_VALID, 'reason': reason}), 400
