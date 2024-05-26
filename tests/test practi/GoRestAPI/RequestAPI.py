
import requests
import random
import json
import string



#base url
base_url = "https://gorest.co.in"

#Auth token:
auth_token = "Bearer f351b799419d1cacd17b4e1eef30c16a3a6a2da86a673eebc5eead3f19edcbdf"

#get random email id:
def generate_random_email():
    domain = "automation.com"
    email_length = 15
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

#Get Request
#Calls all users
def get_request_all():
    url = base_url + "/public/v2/users/"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_payload = response.json()
    json_str = json.dumps(json_payload, indent=4)  #Makes it so that the code prints out in a more readable fashion
    print("json response body: ", json_str)
    print()




#Calls one specific user
def get_request():
    url = base_url + "/public/v2/users/2934642"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_payload = response.json()
    json_str = json.dumps(json_payload, indent=4)  #Makes it so that the code prints out in a more readable fashion
    print("json GET response body: ", json_str)
    print()


#Post Request
def post_request():
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    headers = {"Authorization": auth_token}
    payload = {
        "name": "Ali Z.",
        "email": generate_random_email(),
        "gender": "Female",
        "status": "active"
    }
    response = requests.post(url, payload, headers=headers)
    print(response.status_code)
    json_payload = response.json()
    json_str = json.dumps(json_payload, indent=4)
    print("json POST response body: ", json_str)
    user_id = json_payload["id"]
    print("User id: ",user_id)
    assert response.status_code == 201
    assert "name" in json_payload
    assert json_payload["name"] == "Ali Z."
    print("....USER HAS BEEN CREATED....")
    return user_id




#Put Request
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("put url: " + url)
    headers = {"Authorization": auth_token}
    payload = {
        "name": "Aliooo Pool",
        "email": generate_random_email(),
        "gender": "Female",
        "status": "inactive"
    }
    response = requests.put(url, payload, headers=headers)
    assert response.status_code == 200
    print(response.status_code)
    json_payload = response.json()
    json_str = json.dumps(json_payload, indent=4)
    print("json PUT response body: ", json_str)
    assert json_payload["id"] == user_id
    assert json_payload["name"] == "Aliooo Pool"
    print("....USER INFO HAS BEEN UPDATED....")
    print()

#Delete Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("Delete url: " + url)
    headers = {"Authorization": auth_token}

    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print(response.status_code)
    print("......DELETE USER IS DONE.......")

#Calling section

get_request_all()
#get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)
