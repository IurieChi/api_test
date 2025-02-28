import requests
import logging

logger = logging.getLogger(__name__)  # Logger instance


class SearchApi:

    def check_status_code(self, url, param):
        """check request status_code"""
        try:
            logger.info(f"Sending {param} request to {url}")  # Log request details
            response = requests.get(url, timeout=10)
            logger.info(f"Response: {response.status_code} - {response.text}")
            return response
        except requests.exceptions.HTTPError as e:
            return f"HTTP Error: {e}"
        except requests.exceptions.JSONDecodeError as e:
            logger.error(f"Request failed: {e}")
            return f"The response body does not contain valid json {e}"
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            return f"Request Error: {e}"

    def check_api_req_method(self, url, req_method):
        """Make multiple requests with different methods & log responses"""
        try:
            logger.info(f"Sending {req_method} request to {url}")  # Log request details

            if req_method == "GET":
                response = requests.get(url)
            elif req_method == "POST":
                response = requests.post(url)
            elif req_method == "PUT":
                response = requests.put(url)
            elif req_method == "DELETE":
                response = requests.delete(url)
            elif req_method == "PATCH":
                response = requests.patch(url)
            elif req_method == "OPTIONS":
                response = requests.options(url)
            elif req_method == "HEAD":
                response = requests.head(url)
            else:
                logger.error(f"Invalid request method: {req_method}")
                return None

            logger.info(f"Response: {response.status_code} - {response.text[:200]}")
            return response
        except requests.exceptions.HTTPError as e:
            logger.error(f"Request failed: {e}")
            return f"HTTP Error: {e}"
        except requests.exceptions.JSONDecodeError as e:
            logger.error(f"Request failed: {e}")
            return f"The response body does not contain valid json {e}"
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            return f"Request Error: {e}"
