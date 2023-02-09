# Testing a REST API with Pytest can be done by sending HTTP requests
# to the API and verifying the response. You can use the requests library
# in Python to send HTTP requests and Pytest to write tests
# and verify the responses.
#
# Here's an example of how to test a REST API with Pytest:
import requests


def test_get_users():
    response = requests.get("https://api.example.com/users")
    assert response.status_code == 200
    assert response.json()["users"]


def test_get_user():
    response = requests.get("https://api.example.com/users/1")
    assert response.status_code == 200
    assert response.json()["user"]


def test_create_user():
    response = requests.post("https://api.example.com/users", json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201
    assert response.json()["user"]


def test_update_user():
    response = requests.put("https://api.example.com/users/1", json={
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    })
    assert response.status_code == 200
    assert response.json()["user"]


def test_delete_user():
    response = requests.delete("https://api.example.com/users/1")
    assert response.status_code == 204

# In this example, the requests library is used to send HTTP requests
# to the API. The requests.get method is used to send GET requests,
# requests.post to send POST requests, requests.put to send PUT requests,
# and requests.delete to send DELETE requests.
# The response.status_code attribute is used to verify the HTTP status code
# of the response, and the response.json method is used
# to parse the JSON response. The assert statement is used to verify that
# the response is as expected.
#
# By using Pytest and the requests library, it's possible to write tests
# for a REST API in a simple and straightforward manner.
# You can also use Pytest fixtures to set up and tear down resources
# required by the tests, as well as to share data between tests.
# This can help to make your tests more modular and reusable.
