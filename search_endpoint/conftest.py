import logging
import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Configure logging for pytest."""
    logging.basicConfig(
        level=logging.DEBUG,  # Capture all logs
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("test_logs.log"),  # Save logs to file
            logging.StreamHandler(),  # Print logs to console
        ],
    )
