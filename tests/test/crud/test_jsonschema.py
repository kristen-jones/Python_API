"""
1. Get Response
2. Create the json schema - https://www.jsonschema.net/
3. Save that schema into the name.json file
4. Validate the json schema - https://www.jsonschemavalidator.net/

"""

import pytest
import allure
import os

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from src.constants.api_constants import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import *


class TestCreateBookingJSONSchema(object):

    def load_schema(self, file_name):
        with open(file_name, 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    @allure.title("Verify that create booking status and bookinid shouldn't be null")
    @allure.description("create a booking from the payload and verify that bookingid shouldn't be null and "
                        "status code should be 200 for the correct payload ")
    def test_create_booking_positive_schema(self):
        #URL,Payload, headers
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)

        booking_id = response.json()["bookingid"]

        verify_http_status_code(response, 200)
        verify_json_key_for_not_null(booking_id)

        # verify response with schema.json stored
        file_path = os.getcwd() + "/create_booking_schema.json"
        schema = self.load_schema(file_name=file_path)

        try:
            validate(instance=response.json(), schema=schema)
        except ValidationError as e:
            print(e.message)
            pytest.fail("Failed : JSON schema error")
