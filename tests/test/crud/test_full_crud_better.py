"""
Create Token
Create Booking ID
Update the booking - BookingID, Token
Delete the booking
"""


#Verify that created booking id when we update it and delete it

import pytest
import allure
import logging

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from src.utils.utils import *


class TestCRUDBooking(object):

    @allure.title("Test CRUD operation update(PUT)")
    @allure.description("Verify that full update of the booking ID and token is working")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        booking_id = get_booking_id
        token = create_token
        patch_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_requests(
            url=patch_url,
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )

        logger.info("Request is made" + str(response))
        # Verification here & more
        verify_response_key(response.json()["firstname"], "Kristen")
        verify_response_key(response.json()["lastname"], "Jones")
        verify_http_status_code(response_data=response, expect_data=200)
        logger.info("Request status code" + str(response.status_code))

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

        print(response.status_code)