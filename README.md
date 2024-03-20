# Phone Number Information API

This API service is designed to fetch information about phone numbers, such as the country code, area code, and local phone number. It validates and parses phone numbers provided in E.164 format and can also accept phone numbers with spaces between different segments.

## Installation and Running

Follow these steps to install and run the application:

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the FastAPI application:
```bash
uvicorn main:app --reload
```

This command starts the server on http://127.0.0.1:8000/. The --reload option enables live reloading for development.

3. To run tests, execute:
```bash
pytest test_main.py
```

Ensure the FastAPI application is running before executing the tests, as they make direct HTTP requests to the server.

## Accessing the Application
- API Endpoint: http://127.0.0.1:8000/v1/phone-numbers
- Swagger Documentation: http://127.0.0.1:8000/docs

## Choice of Programming Language, Framework, and Library
- Python: Chosen for its simplicity and the powerful ecosystem of libraries, making it ideal for quickly developing web applications and APIs.
- FastAPI: A modern, fast web framework for building APIs with Python. It is selected for its performance, ease of use, and built-in support for async operations and automatic generation of OpenAPI documentation.
- Uvicorn: An ASGI server for Python, used to serve FastAPI applications. It is lightweight, super-fast, and supports asynchronous I/O.
- Pytest: Used for running tests due to its simplicity and powerful features for writing and organizing tests.

## Deployment to Production
For production deployment, consider the following steps:

- Remove the --reload option from the Uvicorn command to improve performance.
- Ensure all dependencies are securely updated.
- Use a Docker container for deploying the application to ensure environment consistency.
- Place a reverse proxy (e.g., Nginx) in front of Uvicorn for better security and performance.
- Use environment variables for configuration settings, such as database connections or external API keys.
- Consider using cloud services (e.g., AWS, GCP, Azure) for scalability and reliability.

## Assumptions Made

- The phone numbers are primarily in E.164 format but can include spaces for readability.
- Users may not always include the country code, requiring a separate countryCode parameter for such cases.

## Improvements Wishlist
- Implement authentication for API access.
- Add more comprehensive input validation and error handling for edge cases.
- Enhance the test suite with more scenarios and integration tests.
- Introduce a caching mechanism to improve response times for frequently queried phone numbers.
- Add support for batch processing of phone numbers to improve efficiency.