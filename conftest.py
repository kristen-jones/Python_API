import pytest
import allure
import openpyxl

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import *



@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants.url_create_token(),
        headers=Util().common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json=False
        )
    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=APIConstants.url_create_booking(),
        auth=None,
        headers=Util().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False
    )
    booking_id = response.json()["bookingid"]

    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id



@pytest.fixture(scope="session")
def create_booking():
    response = post_request(
        url=APIConstants.url_create_booking(),
        auth=None,
        headers=Util().common_headers_json(),
        payload=payload_create_booking_dynamic(),
        in_json=False
    )
    booking_id = response.json()["bookingid"]

    # Verifications
    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null_token(booking_id)

    return booking_id

@pytest.fixture
def update_payload(self):
    def _update_payload(payload, updates):
        """ Update specific keys in the payload with provided values. """
        payload.update(updates)
        return payload
    return _update_payload


