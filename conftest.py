import logging
import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Configure logging for pytest and ensure logs are written to a file."""

    log_dir = "reports"
    log_file = os.path.join(log_dir, "test_logs.log")

    # Ensure the reports/ directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Capture all logs

    # Remove existing handlers to avoid duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    # File Handler
    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(file_handler)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(console_handler)

    logging.info("✅ Logging successfully set up!")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Hook that runs after each test to check for failure and log the error."""
    if call.excinfo is not None:  # If there was an exception (i.e., test failed)
        # Get the logger
        logger = logging.getLogger()

        # Log only assertion failures
        if isinstance(call.excinfo.value, AssertionError):
            logger.error(f"Assertion failed in test {item.nodeid}!")
            logger.error(
                f"Assertion Error: {call.excinfo.value}"
            )  # Log the assertion error
