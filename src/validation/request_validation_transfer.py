from jsonschema import ValidationError

from validation.request_validation import RequestValidation


class RequestValidationTransfer(RequestValidation):
    JSONSCHEMA_REQUEST_TRANSFER_BACKUP = {
        "type": "object",
        "properties": {
            "code": {"type": "string", "minLength": 10, "maxLength": 10},
            "settings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "quotations": {
                            "type": "object",
                            "properties": {
                                "CONTENT_ADD_TO_PREVIOUS_ALL": {"type": "boolean"},
                                "CONTENT_ALL": {"type": "boolean"},
                                "CONTENT_AUTHOR": {"type": "boolean"},
                                "CONTENT_AUTHOR_NAME": {"type": "string"},
                                "CONTENT_FAVOURITES": {"type": "boolean"},
                                "CONTENT_SEARCH": {"type": "boolean"},
                                "CONTENT_SEARCH_COUNT": {"type": "integer"},
                                "CONTENT_SEARCH_TEXT": {"type": "string"},

                            },
                            "required": [
                                "CONTENT_ADD_TO_PREVIOUS_ALL",
                                "CONTENT_ALL",
                                "CONTENT_AUTHOR",
                                "CONTENT_AUTHOR_NAME",
                                "CONTENT_FAVOURITES",
                                "CONTENT_SEARCH",
                                "CONTENT_SEARCH_COUNT",
                                "CONTENT_SEARCH_TEXT",
                            ],
                        },
                        "appearance": {
                            "type": "object",
                            "properties": {
                                "APPEARANCE_TRANSPARENCY": {"type": "integer"},
                                "APPEARANCE_COLOUR": {"type": "string"},
                                "APPEARANCE_TEXT_FAMILY": {"type": "string"},
                                "APPEARANCE_TEXT_STYLE": {"type": "string"},
                                "APPEARANCE_TEXT_FORCE_ITALIC_REGULAR": {"type": "boolean"},
                                "APPEARANCE_TEXT_SIZE": {"type": "integer"},
                                "APPEARANCE_TEXT_COLOUR": {"type": "string"},
                                "APPEARANCE_AUTHOR_TEXT_SIZE": {"type": "integer"},
                                "APPEARANCE_AUTHOR_TEXT_COLOUR": {"type": "string"},
                                "APPEARANCE_AUTHOR_TEXT_HIDE": {"type": "boolean"},
                                "APPEARANCE_POSITION_TEXT_SIZE": {"type": "integer"},
                                "APPEARANCE_POSITION_TEXT_COLOUR": {"type": "string"},
                                "APPEARANCE_POSITION_TEXT_HIDE": {"type": "boolean"},
                                "APPEARANCE_REMOVE_SPACE_ABOVE_TOOLBAR": {"type": "boolean"},
                                "APPEARANCE_TOOLBAR_COLOUR": {"type": "string"},
                                "APPEARANCE_TOOLBAR_FIRST": {"type": "boolean"},
                                "APPEARANCE_TOOLBAR_PREVIOUS": {"type": "boolean"},
                                "APPEARANCE_TOOLBAR_FAVOURITE": {"type": "boolean"},
                                "APPEARANCE_TOOLBAR_SHARE": {"type": "boolean"},
                                "APPEARANCE_TOOLBAR_RANDOM": {"type": "boolean"},
                                "APPEARANCE_TOOLBAR_SEQUENTIAL": {"type": "boolean"}
                            },
                            "required": [
                                "APPEARANCE_TRANSPARENCY",
                                "APPEARANCE_COLOUR",
                                "APPEARANCE_TEXT_FAMILY",
                                "APPEARANCE_TEXT_STYLE",
                                "APPEARANCE_TEXT_SIZE",
                                "APPEARANCE_TEXT_COLOUR",
                                "APPEARANCE_TOOLBAR_COLOUR",
                                "APPEARANCE_TOOLBAR_FIRST",
                                "APPEARANCE_TOOLBAR_PREVIOUS",
                                "APPEARANCE_TOOLBAR_FAVOURITE",
                                "APPEARANCE_TOOLBAR_SHARE",
                                "APPEARANCE_TOOLBAR_RANDOM",
                                "APPEARANCE_TOOLBAR_SEQUENTIAL"
                            ],
                        },
                        "schedule": {
                            "type": "object",
                            "properties": {
                                "EVENT_NEXT_RANDOM": {"type": "boolean"},
                                "EVENT_NEXT_SEQUENTIAL": {"type": "boolean"},
                                "EVENT_DISPLAY_WIDGET": {"type": "boolean"},
                                "EVENT_DISPLAY_WIDGET_AND_NOTIFICATION": {"type": "boolean"},
                                "EVENT_DAILY": {"type": "boolean"},
                                "EVENT_DEVICE_UNLOCK": {"type": "boolean"},
                                "EVENT_DAILY_MINUTE": {"type": "integer"},
                                "EVENT_DAILY_HOUR": {"type": "integer"}
                            },
                            "required": [
                                "EVENT_NEXT_RANDOM",
                                "EVENT_NEXT_SEQUENTIAL",
                                "EVENT_DISPLAY_WIDGET",
                                "EVENT_DISPLAY_WIDGET_AND_NOTIFICATION",
                                "EVENT_DAILY",
                                "EVENT_DEVICE_UNLOCK",
                                "EVENT_DAILY_MINUTE",
                                "EVENT_DAILY_HOUR"
                            ],
                        },
                        "widget_id": {"type": "integer"},
                    },
                },
            },
            "current": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "digest": {"$ref": "#/$defs/digest"},
                        "widget_id": {"$ref": "#/$defs/widget_id"},
                    },
                    "required": [
                        "digest",
                        "widget_id",
                    ]
                }
            },
            "previous": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "content_type": {"type": "integer"},
                        "digest": {"$ref": "#/$defs/digest"},
                        "navigation": {"$ref": "#/$defs/navigation"},
                        "widget_id": {"$ref": "#/$defs/widget_id"}
                    },
                    "required": [
                        "content_type",
                        "digest",
                        "navigation",
                        "widget_id"
                    ]
                }
            },
            "favourite": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "digest": {"$ref": "#/$defs/digest"},
                        "navigation": {"$ref": "#/$defs/navigation"},
                    },
                    "required": [
                        "digest",
                        "navigation",
                    ]
                }
            },
        },
        "$defs": {
            "digest": {"type": "string", "minLength": 8, "maxLength": 8},
            "navigation": {"type": "integer"},
            "widget_id": {"type": "integer"}
        },
        "required": ["code", "settings", "current", "previous", "favourite"]
    }

    def check_request_transfer_backup(self, request):
        invalid_code_response = self._check_code(request)
        if invalid_code_response is not None:
            return self.report_error_with_request(invalid_code_response)

        try:
            self.check_against_jsonschema(request.json, self.JSONSCHEMA_REQUEST_TRANSFER_BACKUP)
        except ValidationError as e:
            return self.report_error_with_request(e.message)

        return None
