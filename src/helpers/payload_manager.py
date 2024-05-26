#payloads
#dict -->

import json
from faker import Faker

faker = Faker()


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
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": faker.date(),
            "checkout": faker.date()
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "Lunch"))
    }
    return payload


def payload_update_booking(*fields_to_update):
    payload_options = {
        "firstname": faker.first_name,
        "lastname": faker.last_name,
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": faker.boolean,
        "bookingdates": {
            "checkin": faker.date(),
            "checkout": faker.date()
        },
        "additionalneeds":faker.random_element(elements=("Breakfast", "Parking", "Lunch"))
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
