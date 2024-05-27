import pytest
import requests
import json
from src.helpers.payload_manager import create_user, update_user, delete_user
from faker import Faker

fake = Faker()


class ApiRequests:
    # base url
    base_url = "https://gorest.co.in"
    # Auth token:
    auth_token = "Bearer f351b799419d1cacd17b4e1eef30c16a3a6a2da86a673eebc5eead3f19edcbdf"

    # Get Request
    # Calls all users
    def test_get_request_all(self):
        url = self.base_url + "/public/v2/users/"
        headers = {"Authorization": self.auth_token}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        json_payload = response.json()
        json_str = json.dumps(json_payload, indent=4)  # Makes it so that the code prints out in a more readable fashion
        print("json response body: ", json_str)

        print()
        print()

    #Calls one specific user
    def test_get_request(self):
        url = self.base_url + "/public/v2/users/2934642"
        headers = {"Authorization": self.auth_token}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        json_payload = response.json()
        json_str = json.dumps(json_payload, indent=4)  #Makes it so that the code prints out in a more readable fashion
        print("json GET response body: ", json_str)

        print()
        print()

    def test_create_update_delete_user(self):
        """Integration test: Create a user, update the user, and delete the user."""
        user_id, create_response = create_user(self.base_url, self.auth_token)
        print("User created:", create_response)
        update_response = update_user(self.base_url, self.auth_token, user_id)
        print("User updated:", update_response)
        delete_status_code = delete_user(self.base_url, self.auth_token, user_id)
        print("User deleted with status code:", delete_status_code)

        print()
        print()

    def test_create_and_retrieve_user(self):
        """Integration test: Create a user and retrieve the user's details."""
        user_id, create_response = create_user(self.base_url, self.auth_token)
        print("User created:", create_response)
        url = self.base_url + f"/public/v2/users/{user_id}"
        headers = {"Authorization": self.auth_token}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        print("User retrieved:", response.json())
        delete_status_code = delete_user(self.base_url, self.auth_token, user_id)
        print("User deleted with status code:", delete_status_code)

        print()
        print()

    def test_create_update_and_verify_user(self):
        """Integration test: Create a user, update the user, and verify the updated details."""
        user_id, create_response = create_user(self.base_url, self.auth_token)
        print("User created:", create_response)
        update_response = update_user(self.base_url, self.auth_token, user_id)
        print("User updated:", update_response)
        url = self.base_url + f"/public/v2/users/{user_id}"
        headers = {"Authorization": self.auth_token}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        print("Updated user details:", response.json())
        delete_status_code = delete_user(self.base_url, self.auth_token, user_id)
        print("User deleted with status code:", delete_status_code)

        print()
        print()

    def test_create_and_delete_user(self):
        """Integration test: Create a user and then delete the user."""
        user_id, create_response = create_user(self.base_url, self.auth_token)
        print("User created:", create_response)
        delete_status_code = delete_user(self.base_url, self.auth_token, user_id)
        print("User deleted with status code:", delete_status_code)
        url = self.base_url + f"/public/v2/users/{user_id}"
        headers = {"Authorization": self.auth_token}
        response = requests.get(url, headers=headers)
        assert response.status_code == 404
        print("User deletion confirmed. User not found.")

        print()
        print()

    def test_create_user_with_duplicate_email(self):
        """Integration test: Create a user and attempt to create another user with the same email."""
        user_id, create_response = create_user(self.base_url, self.auth_token)
        print("User created:", create_response)
        payload = {
            "name": fake.name(),
            "email": create_response["email"],
            "gender": "Female",
            "status": "active"
        }
        url = self.base_url + "/public/v2/users"
        #print("User with same email: "payload)
        print()
        print()

    def test_integration_scenario_4(self):
        """Test Integration Scenario 4: Create user, update user, create another user, delete both users."""
        user1_id, create_response = create_user(self.base_url, self.auth_token)
        print("User created:", create_response)
        update_response = update_user(self.base_url, self.auth_token, user1_id)
        print("User updated:", update_response)
        user2_id, create_response = create_user(self.base_url, self.auth_token)
        print("User created:", create_response)
        delete_status_code1 = delete_user(self.base_url, self.auth_token, user1_id)
        delete_status_code2 = delete_user(self.base_url, self.auth_token, user2_id)
        print("Both users deleted: ", delete_status_code1, delete_status_code2)

        print()
        print()

    def test_integration_scenario_5(self):
        """Test Integration Scenario 5: Create user, update user, update again, delete user."""
        user_id, create_response = create_user(self.base_url, self.auth_token)
        print("User created:", create_response)
        update_response = update_user(self.base_url, self.auth_token, user_id)
        print("User updated:", update_response)
        update_response2 = update_user(self.base_url, self.auth_token, user_id)
        print("User updated:", update_response2)
        delete_status_code = delete_user(self.base_url, self.auth_token, user_id)
        print(delete_status_code)



api_test = ApiRequests()

api_test.test_get_request_all()
api_test.test_get_request()
api_test.test_create_update_delete_user()
api_test.test_create_and_retrieve_user()
api_test.test_create_update_and_verify_user()
api_test.test_create_and_delete_user()
api_test.test_create_user_with_duplicate_email()
api_test.test_integration_scenario_4()
api_test.test_integration_scenario_5()
