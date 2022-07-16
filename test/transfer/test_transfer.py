from validation.request_validation_transfer import RequestValidationTransfer

json_request = {
    "code": "200000005e",
    "settings": [
        {
            "quotations": {
                "CONTENT_ADD_TO_PREVIOUS_ALL": True,
                "CONTENT_ALL": True,
                "CONTENT_AUTHOR": False,
                "CONTENT_AUTHOR_NAME": "",
                "CONTENT_FAVOURITES": False,
                "CONTENT_SEARCH": False,
                "CONTENT_SEARCH_COUNT": 0,
                "CONTENT_SEARCH_TEXT": ""
            },
            "appearance": {
                "APPEARANCE_TRANSPARENCY": 0,
                "APPEARANCE_COLOUR": "",
                "APPEARANCE_TEXT_FAMILY": "",
                "APPEARANCE_TEXT_STYLE": "",
                "APPEARANCE_TEXT_SIZE": 0,
                "APPEARANCE_TEXT_COLOUR": "",
                "APPEARANCE_TOOLBAR_COLOUR": "",
                "APPEARANCE_TOOLBAR_FIRST": False,
                "APPEARANCE_TOOLBAR_PREVIOUS": True,
                "APPEARANCE_TOOLBAR_FAVOURITE": True,
                "APPEARANCE_TOOLBAR_SHARE": True,
                "APPEARANCE_TOOLBAR_RANDOM": True,
                "APPEARANCE_TOOLBAR_SEQUENTIAL": False
            },
            "schedule": {
                "EVENT_NEXT_RANDOM": False,
                "EVENT_NEXT_SEQUENTIAL": True,
                "EVENT_DISPLAY_WIDGET": False,
                "EVENT_DISPLAY_WIDGET_AND_NOTIFICATION": True,
                "EVENT_DAILY": False,
                "EVENT_DEVICE_UNLOCK": False,
                "EVENT_DAILY_MINUTE": 0,
                "EVENT_DAILY_HOUR": 0
            },
            "widget_id": 12
        },
        {
            "quotations": {
                "CONTENT_ADD_TO_PREVIOUS_ALL": True,
                "CONTENT_ALL": True,
                "CONTENT_AUTHOR": False,
                "CONTENT_AUTHOR_NAME": "",
                "CONTENT_FAVOURITES": False,
                "CONTENT_SEARCH": False,
                "CONTENT_SEARCH_COUNT": 0,
                "CONTENT_SEARCH_TEXT": ""
            },
            "appearance": {
                "APPEARANCE_TRANSPARENCY": 0,
                "APPEARANCE_COLOUR": "",
                "APPEARANCE_TEXT_FAMILY": "",
                "APPEARANCE_TEXT_STYLE": "",
                "APPEARANCE_TEXT_SIZE": 0,
                "APPEARANCE_TEXT_COLOUR": "",
                "APPEARANCE_TOOLBAR_COLOUR": "",
                "APPEARANCE_TOOLBAR_FIRST": False,
                "APPEARANCE_TOOLBAR_PREVIOUS": True,
                "APPEARANCE_TOOLBAR_FAVOURITE": True,
                "APPEARANCE_TOOLBAR_SHARE": True,
                "APPEARANCE_TOOLBAR_RANDOM": True,
                "APPEARANCE_TOOLBAR_SEQUENTIAL": False
            },
            "schedule": {
                "EVENT_NEXT_RANDOM": False,
                "EVENT_NEXT_SEQUENTIAL": True,
                "EVENT_DISPLAY_WIDGET": False,
                "EVENT_DISPLAY_WIDGET_AND_NOTIFICATION": True,
                "EVENT_DAILY": False,
                "EVENT_DEVICE_UNLOCK": False,
                "EVENT_DAILY_MINUTE": 0,
                "EVENT_DAILY_HOUR": 0
            },
            "widget_id": 13
        },
    ],
    "current": [
        {
            "digest": "bb4685f4",
            "widget_id": 12
        },
        {
            "digest": "1a2dbc82",
            "widget_id": 13
        }
    ],
    "previous": [
        {
            "content_type": 1,
            "digest": "7a36e553",
            "navigation": 1,
            "widget_id": 12
        },
        {
            "content_type": 1,
            "digest": "7a36e553",
            "navigation": 2,
            "widget_id": 13
        },
    ],
    "favourite": [
        {
            "digest": "bb4685f4",
            "navigation": 1
        },
        {
            "digest": "1a2dbc82",
            "navigation": 2
        }
    ],
}


def test_valid_backup_request(client):
    response = client.post('/transfer_backup', json=json_request)
    assert not response.is_json
    assert response.status_code == 200


def test_valid_restore_request(client):
    response = client.post('/transfer_restore', json={
        "code": "200000005e",
    })

    assert response.is_json
    assert response.json['transfer']["code"] == json_request["code"]
    assert response.json['transfer']["settings"] == json_request["settings"]
    assert response.json['transfer']["current"] == json_request["current"]
    assert response.json['transfer']["previous"] == json_request["previous"]
    assert response.json['transfer']["favourite"] == json_request["favourite"]
    assert response.status_code == 200


def test_valid_request_but_unknown_code(client):
    response = client.post('/transfer_restore', json={'code': '6000000061'})

    assert response.is_json
    assert response.json['transfer'] == {}
    assert response.json['error'] == RequestValidationTransfer.RESPONSE_ERROR_JSON_NOT_VALID
    assert response.json['reason'] == RequestValidationTransfer.RESPONSE_REASON_NO_JSON_FOR_CODE
    assert response.status_code == 400
