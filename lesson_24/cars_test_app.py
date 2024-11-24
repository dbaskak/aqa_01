import pytest
import logging
import os
import requests
from requests.auth import HTTPBasicAuth

# Set up logging with both file and console output
log_file_path = os.path.join(os.getcwd(), "test_search.log")

# Configure logging
logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(console_handler)

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="class")
def auth_session():
    """Fixture to authenticate and create a session with a valid access token."""
    session = requests.Session()
    auth = HTTPBasicAuth("test_user", "test_pass")
    response = session.post(f"{BASE_URL}/auth", auth=auth)

    # Log current working directory
    logger.info(f"Current working directory: {os.getcwd()}")

    # Ensure authentication was successful
    assert response.status_code == 200, "Authentication failed!"
    token = response.json().get("access_token")
    assert token, "Access token was not retrieved!"

    # Add token to session headers
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session

@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 10),
    (None, 7),
    ("brand", None),
    (None, None),
])
def test_search_cars(auth_session, sort_by, limit):
    """Test the /cars endpoint with various parameters."""
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    response = auth_session.get(f"{BASE_URL}/cars", params=params)

    # Logging the request and response status
    logging.info(f"GET /cars with parameters {params} - Status {response.status_code}")

    # Ensure the request was successful
    assert response.status_code == 200, "Request was not successful!"
    data = response.json()
    logging.info(f"Response data: {data}")

    # Validate the response data
    if limit:
        assert len(data) <= limit, "Number of records exceeds the limit!"

    if sort_by:
        sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0))
        assert data == sorted_data, "Data is not sorted correctly!"