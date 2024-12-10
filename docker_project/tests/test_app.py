import pytest
import allure
from app import app


@pytest.fixture
def client():
    return app.test_client()


@allure.feature("API Tests")
@allure.story("Home Endpoint")
def test_home(client):
    with allure.step("Send GET request to '/' endpoint"):
        response = client.get('/')

    with allure.step("Check the status code"):
        assert response.status_code == 200

    with allure.step("Validate the response message"):
        assert response.json['message'] == "Connected to database mydb!"


@allure.feature("API Tests")
@allure.story("Add Record Endpoint")
def test_add_record(client):
    with allure.step("Send POST request to '/add' endpoint with test data"):
        response = client.post('/add', json={"name": "TestUser", "age": 30})

    with allure.step("Check the status code"):
        assert response.status_code == 201

    with allure.step("Validate the response contains an ID"):
        assert "id" in response.json