"""
Create Token
Create Booking ID
Update the booking - BookingID, Token
Delete the booking
"""

#Verify that created booking id when we update it and delete it

import pytest
import allure

from src.constants.api_constants import *
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from src.utils.utils import *


class TestCRUDBooking(object):


    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(),
                                headers=Util().common_headers_json(),
                                auth=None,
                                payload=payload_create_token(),
                                in_json=False
                                )
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null_token(response.json()["token"])
        return response.json()["token"]

    @pytest.fixture
    def get_booking_id(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)

        booking_id = response.json()["bookingid"]

        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id

    @allure.title("Test CRUD operation update(PUT)")
    @allure.description("Verify that full update of the booking ID and token is working")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_requests(
            url=put_url,
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )
        # Verification here & more
        verify_response_key(response.json()["firstname"], "Kristen")
        verify_response_key(response.json()["lastname"], "Jones")
        verify_http_status_code(response_data=response, expect_data=200)

    @allure.title("Test CRUD operation delete(DELETE)")
    @allure.description("Verify that booking gets deleted with the booking ID and token is working")
    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_requests(
            url=delete_url,
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expect_data=201)
