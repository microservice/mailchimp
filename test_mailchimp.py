from http import HTTPStatus
import os

USER_EMAIL=os.getenv('USER_EMAIL')

def test_add_to_list_request(client):
    data = {
        "listName": "microservices",
        "userEmail":USER_EMAIL,
        "status":"subscribed",
        "firstName":"James",
        "lastName":"Anderson",
    }
    url = "/subscribers/add"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_add_to_list_request_fail(client):
    data = {
        "listName": "microservice",
        "userEmail":USER_EMAIL,
        "status":"subscribed",
        "firstName":"James",
        "lastName":"Anderson",
    }
    url = "/subscribers/add"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

def test_add_tags_request(client):
    data = {
        "listName": "microservices",
        "userEmail":USER_EMAIL,
        "tags":"imortal"
    }
    url = "/tags"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK    

def test_update_subscriber_request(client):
    data = {
        "listName": "microservices",
        "userEmail":USER_EMAIL,
        "status":"subscribed",
        "firstName":"James",
        "lastName":"Anderson",
    }
    url = "/subscribers/updatesubscriber"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK


def test_delete_from_list_request(client):
    data = {
        "listName": "microservices",
        "userEmail":USER_EMAIL,
    }
    url = "/subscribers/delete"
    response = client.post(url,json=data)
    assert response.status_code == HTTPStatus.OK    