import json

import pytest
import allure

from src.constants.api_constants import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import *


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that create booking status and bookinid shouldn't be null")
    @allure.description("create a booking from the payload and verify that bookingid shouldn't be null and "
                        "status code should be 200 for the correct payload ")
    def test_create_booking_positive(self):
        #URL,Payload, headers
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)

        booking_id = response.json()["bookingid"]

        verify_http_status_code(response, 200)
        verify_json_key_for_not_null(booking_id)

    @pytest.mark.negative
    def test_create_booking_tc2(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload={},
                                in_json=False)
        verify_http_status_code(response, 500)
