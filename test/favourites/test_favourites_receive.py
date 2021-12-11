from validation.request_validation_favourites import RequestValidationFavourites


def test_http_get_not_supported(client):
    assert client.get("/receive").status_code == 405


def test_invalid_receive_request(client):
    response = client.post('/receive', json={'code': ''})
    assert response.json['error'] == RequestValidationFavourites.RESPONSE_ERROR_JSON_NOT_VALID
    assert response.json['reason'] == RequestValidationFavourites.RESPONSE_REASON_LENGTH_CODE
    assert response.status_code == 400


def test_valid_request_but_unknown_code(client):
    response = client.post('/receive', json={'code': '1234567825'})
    assert response.json['error'] == RequestValidationFavourites.RESPONSE_ERROR_JSON_NOT_VALID
    assert response.json['reason'] == RequestValidationFavourites.RESPONSE_REASON_NO_JSON_FOR_CODE
    assert response.status_code == 400


def test_valid_request(client):
    # NOTE: it takes n seconds for Firestore database to be viewable
    response = client.post('/receive', json={'code': "10000000d1"})
    assert response.is_json
    assert response.json['digests'] == ['01234567', '12345678']
    assert response.status_code == 200
