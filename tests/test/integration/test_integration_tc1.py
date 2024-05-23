"""
Integration Scenarios
Verify that create booking --> Patch Request - Verify that firstName
Create a booking, Delete the booking with ID and Verify using GET request that
3. Get an existing booking id from get all booking ids, Update a booking
"""

import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from src.utils.utils import *


class testIntergrationBooking(object):

    @pytest.mark.positive
    @allure.title("Create a booking")
    @allure.description("Create a booking")
    def test_create_booking(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_token(),
                                in_json=False)

        booking_id = response.json()["bookingid"]
        actual_status_code = response.status_code

        verify_http_status_code(response_data=actual_status_code, expect_data=200)
        verify_json_key_for_not_null_token(booking_id)

    @pytest.mark.positive
    @allure.title("Update the booking name")
    @allure.description("Update the name of the booking that was created")
    def test_update_booking(self):
        pass

    @pytest.mark.positive
    @allure.title("Get the booking by ID and Verify")
    @allure.description("Verify the ID of the booking that was created")
    def test_get_specific_booking(self):
        pass
