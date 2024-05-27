#payloads
#dict -->

import json
import requests
from faker import Faker

fake = Faker()


def payload_create_booking():
    payload = {
        "firstname": "Null",
        "lastname": "Null",
        "totalprice": 1223,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_booking_dynamic():
    payload = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": fake.date(),
            "checkout": fake.date()
        },
        "additionalneeds": fake.random_element(elements=("Breakfast", "Parking", "Lunch"))
    }
    return payload


def payload_update_booking(*fields_to_update):
    payload_options = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": fake.date(),
            "checkout": fake.date()
        },
        "additionalneeds": fake.random_element(elements=("Breakfast", "Parking", "Lunch"))
    }

    # Generate the payload using a dictionary comprehension
    payload = {field: payload_options[field] for field in fields_to_update if field in payload_options}

    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


#Helpers for GoRestAPI

def create_user(base_url, auth_token):
    """Helper method to create a user and return the user ID."""
    url = base_url + "/public/v2/users"
    headers = {"Authorization": auth_token}
    payload = {
        "name": fake.name(),
        "email": fake.email(),
        "gender": "Female",
        "status": "active"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201
    return response.json()["id"], response.json()


def update_user(base_url, auth_token, user_id):
    """Helper method to update a user's information."""
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    payload = {
        "name": fake.name(),
        "email": fake.email(),
        "gender": "Male",
        "status": "inactive"
    }
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200
    return response.json()


def delete_user(base_url, auth_token, user_id):
    """Helper method to delete a user."""
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    return response.status_code