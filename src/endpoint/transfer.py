from flask import Response, jsonify

from storage import transfer_adapter
from storage.unable_to_send_exception import UnableToSendException
from validation.request_validation_transfer import RequestValidationTransfer


def transfer_backup(request):
    request_validation = RequestValidationTransfer()

    invalid_request_response = request_validation.check_request_transfer_backup(request)
    if invalid_request_response is not None:
        return invalid_request_response

    try:
        transfer_adapter.transfer_backup(request)
        return Response(status=200)
    except UnableToSendException as e:
        return request_validation.report_error_with_request(e.message)


def transfer_restore(request):
    request_validation = RequestValidationTransfer()

    invalid_request_response = request_validation.check_request_receive(request)
    if invalid_request_response is not None:
        return jsonify(
            {
                'transfer': {},
                'error': RequestValidationTransfer.RESPONSE_ERROR_JSON_NOT_VALID,
                'reason': invalid_request_response}
        ), 400

    retrieved_json = transfer_adapter.transfer_restore(request)
    if retrieved_json is not None:
        return retrieved_json, 200
    else:
        return jsonify(
            {
                'transfer': {},
                'error': RequestValidationTransfer.RESPONSE_ERROR_JSON_NOT_VALID,
                'reason': RequestValidationTransfer.RESPONSE_REASON_NO_JSON_FOR_CODE
            }
        ), 400
