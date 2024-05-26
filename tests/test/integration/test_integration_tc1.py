"""
Integration Scenario
Verify that create booking --> Patch Request - Verify that firstName is updated

"""

import allure
import pytest
import logging

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from src.utils.utils import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestIntegrationBooking(object):
    @pytest.mark.positive
    @allure.title("Create a booking")
    @allure.description("Create a booking")
    def test_create_booking(self, create_booking):
        logger.info(f"Booking created:  {create_booking}")

    @pytest.mark.positive
    @allure.title("Partial update: Update the booking name")
    @allure.description("Update the name of the booking that was created")
    def test_update_booking(self, create_booking, create_token):
        booking_id = create_booking
        token = create_token
        patch_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        updated_fields = ["firstname", "lastname"]
        updated_name_payload = payload_update_booking(*updated_fields)

        response = patch_requests(
            url=patch_url,
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            payload=updated_name_payload,
            auth=None,
            in_json=False
        )

        # Verify response status code
        verify_http_status_code(response_data=response, expect_data=200)

        # Extract updated names from response
        response_json = response.json()
        updated_firstname = response_json.get("firstname")
        updated_lastname = response_json.get("lastname")

        # Assert updated names match the payload
        assert updated_firstname == updated_fields["firstname"], "First name update verification failed"
        assert updated_lastname == updated_fields["lastname"], "Last name update verification failed"

        # Log the result
        logger.info(
            f"Booking ID {booking_id} updated with new first name: {updated_firstname} and last name: {updated_lastname}")
        logger.info(f"Request status code: {response.status_code}")

    @pytest.mark.positive
    @allure.title("Get the booking by ID and Verify that first name was updated successfully")
    @allure.description("Verify the ID of the booking that was created")
    def test_get_specific_booking(self):
        pass
