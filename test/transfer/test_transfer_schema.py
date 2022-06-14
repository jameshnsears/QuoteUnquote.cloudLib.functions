import pytest
from jsonschema import ValidationError

from validation.request_validation_transfer import RequestValidationTransfer


def test_valid_transfer_schema_with_new_appearance_elements():
    json_in_request = {
        "code": "qski!$£90d",
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
                    "CONTENT_SEARCH_TEXT": "",
                },
                "appearance": {
                    "APPEARANCE_TRANSPARENCY": 0,
                    "APPEARANCE_COLOUR": "",
                    "APPEARANCE_TEXT_FAMILY": "",
                    "APPEARANCE_TEXT_STYLE": "",
                    "APPEARANCE_TEXT_SIZE": 0,
                    "APPEARANCE_TEXT_COLOUR": "",
                    "APPEARANCE_AUTHOR_TEXT_SIZE": 0,
                    "APPEARANCE_AUTHOR_TEXT_COLOUR": "",
                    "APPEARANCE_AUTHOR_TEXT_HIDE": False,
                    "APPEARANCE_POSITION_TEXT_SIZE": 0,
                    "APPEARANCE_POSITION_TEXT_COLOUR": "",
                    "APPEARANCE_POSITION_TEXT_HIDE": False,
                    "APPEARANCE_REMOVE_SPACE_ABOVE_TOOLBAR": False,
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
                    "CONTENT_SEARCH_TEXT": "",
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

    requestValidationTransfer = RequestValidationTransfer()

    assert requestValidationTransfer.check_against_jsonschema(
        json_in_request,
        RequestValidationTransfer.JSONSCHEMA_REQUEST_TRANSFER_BACKUP) is None


def test_valid_transfer_schema():
    json_in_request = {
        "code": "qski!$£90d",
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
                    "CONTENT_SEARCH_TEXT": "",
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
                    "CONTENT_SEARCH_TEXT": "",
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

    requestValidationTransfer = RequestValidationTransfer()

    assert requestValidationTransfer.check_against_jsonschema(
        json_in_request,
        RequestValidationTransfer.JSONSCHEMA_REQUEST_TRANSFER_BACKUP) is None


def test_invalid_transfer_schema():
    json_in_request = {
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
                    "CONTENT_SEARCH_TEXT": "",
                },
                "appearance": {
                    "APPEARANCE_TRANSPARENCY": 0,
                    "APPEARANCE_COLOUR": "",
                    "APPEARANCE_TEXT_FAMILY": "",
                    "APPEARANCE_TEXT_STYLE": "",
                    "APPEARANCE_TEXT_FORCE_ITALIC_REGULAR": False,
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
        ],
        "favourite": [
            {
                "digest": "bb4685f4",
                "navigation": 1
            },
        ],
    }

    requestValidationTransfer = RequestValidationTransfer()

    with pytest.raises(ValidationError) as validation_error_exception:
        requestValidationTransfer.check_against_jsonschema(
            json_in_request,
            RequestValidationTransfer.JSONSCHEMA_REQUEST_TRANSFER_BACKUP)

    assert validation_error_exception.value.message == "'code' is a required property"
