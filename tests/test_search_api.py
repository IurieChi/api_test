import pytest
import logging
import requests
from utils.search_endpoint import SearchApi
import responses  # Mocks API responses using the responses library
from config.config import (
    base_url,
    search_endpoint,
    req_methods,
    endpoint,
    endpoint_tests,
)


logger = logging.getLogger(__name__)


instance = SearchApi()


@pytest.mark.parametrize("endpoint, params, expected_status", endpoint)
def test_api_search(endpoint, params, expected_status, caplog):
    url = base_url + endpoint + params

    with caplog.at_level(logging.INFO):  # Capture logs at INFO level
        response = instance.check_status_code(url, params)

    # Log test results
    logger.info(f"Tested {params} -> Expected: {expected_status}, Got: {response}")

    assert response.status_code == expected_status


@pytest.mark.parametrize("endpoint, params, expected_status", endpoint_tests)
@responses.activate  # Mocks API responses using the responses library
def test_mock_codes(endpoint, params, expected_status, caplog):
    url = base_url + endpoint + params
    # Mock the API response
    responses.add(responses.GET, url, status=expected_status)

    with caplog.at_level(logging.INFO):  # Capture logs at INFO level
        response = instance.check_status_code(url, params)

    # Log test results
    logger.info(f"Tested {params} -> Expected: {expected_status}, Got: {response}")

    assert response.status_code == expected_status


@pytest.mark.parametrize("method, expected_status", req_methods)
def test_api_methods(method, expected_status, caplog):
    """Test API request methods & log results"""
    url = base_url + search_endpoint

    with caplog.at_level(logging.INFO):  # Capture logs at INFO level
        response = instance.check_api_req_method(url, method)

    try:
        result = response.json()
    except requests.exceptions.JSONDecodeError:
        result = response.text
    # Log test results
    logger.info(f"Tested {method} -> Expected: {expected_status}, Got: {result}")

    assert response.status_code == expected_status
