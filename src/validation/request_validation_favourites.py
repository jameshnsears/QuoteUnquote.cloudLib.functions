from flask import jsonify
from jsonschema import ValidationError

from validation.request_validation import RequestValidation


class RequestValidationFavourites(RequestValidation):
    JSONSCHEMA_FAVOURITES_SEND_REQUEST = {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "minLength": 10,
                "maxLength": 10
            },
            "digests": {
                "type": "array",
                "items": {
                    "type": "string",
                    "minLength": 8,
                    "maxLength": 8
                },
                "minItems": 1,
                "uniqueItems": True
            },
        },
        "required": ["code", "digests"]
    }

    RESPONSE_REASON_LENGTH_DIGESTS = 'digests length'
    RESPONSE_REASON_NO_DIGESTS = 'no digests'

    def check_request_send(self, request):
        invalid_code_response = self._check_code(request)
        if invalid_code_response is not None:
            return invalid_code_response

        if request.json.get('digests', None) is None:
            return self.report_error_with_request(self.RESPONSE_REASON_NO_DIGESTS)

        if len(request.json.get('digests')) == 0:
            return self.report_error_with_request(self.RESPONSE_REASON_LENGTH_DIGESTS)

        try:
            self.check_against_jsonschema(request.json,
                                          self.JSONSCHEMA_FAVOURITES_SEND_REQUEST)
        except ValidationError as e:
            return self.report_error_with_request(e.message)

        return None

    def report_error_with_completing_send(self):
        return jsonify({'error': self.RESPONSE_ERROR_UNABLE_TO_COMPLETE_SEND}), 400
