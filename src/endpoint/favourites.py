from flask import Response

from storage import favourites_adapter
from storage.unable_to_send_exception import UnableToSendException
from validation.request_validation_favourites import RequestValidationFavourites


def favourites_send(request):
    request_validation = RequestValidationFavourites()
    invalid_request_response = request_validation.check_request_send(request)
    if invalid_request_response is not None:
        return invalid_request_response

    try:
        favourites_adapter.favourites_send(request)
        return Response(status=200)
    except UnableToSendException:
        return request_validation.report_error_with_completing_send()


def favourites_receive(request):
    request_validation = RequestValidationFavourites()
    invalid_request_response = request_validation.check_request_receive(request)
    if invalid_request_response is not None:
        return invalid_request_response

    retrieved_digests = favourites_adapter.favourites_retrieve(request)
    if retrieved_digests is not None:
        return retrieved_digests, 200
    else:
        return request_validation.report_error_with_request(
            RequestValidationFavourites.RESPONSE_REASON_NO_JSON_FOR_CODE)
