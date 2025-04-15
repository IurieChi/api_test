base_url = "http://peviitorqa.go.ro/api/v0/"
search_endpoint = "search/"
random_endpoint = "random/"
toal_endpoint = "total/"

# Define API test cases parameterized method
req_methods = [
    ("GET", 200),
    ("POST", 405),
    ("PUT", 405),
    ("DELETE", 405),
    ("PATCH", 405),
    ("OPTIONS", 405),  # OPTIONS usually returns 200
    ("HEAD", 405),  # HEAD usually returns 200
]
# Define API test cases parameters
search_endpoint_parameters = [
    ("search/", "?query=developer", 400),
    ("search/", "?query=engineer", 400),
    ("search/", "?q= ", 200),
    ("search/", "?query=tester", 400),
    ("search/", "?r=manager", 400),
    ("search/", "?ssl=engineer", 400),
    ("searc/", "?query=&", 404),
]

# Define API test cases Error cases
search_endpoint_server_errors = [
    ("search/", "?query=backend", 500),  # Internal Server Error
    ("search/", "?query=frontend", 502),  # Bad Gateway
    ("search/", "?query=database", 503),  # Service Unavailable
    ("search/", "?query=bigdata", 507),  # Insufficient Storage
]


# Define the adjusted JSON schema for response validation
response_schema = {
    "type": "object",
    "properties": {
        "response": {
            "type": "object",
            "properties": {
                "numFound": {"type": "integer"},
                "docs": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "job_title": {"type": "array", "items": {"type": "string"}},
                            "company": {"type": "array", "items": {"type": "string"}},
                            "city": {"type": "array", "items": {"type": "string"}},
                            "remote": {"type": "string"},
                            "job_link": {
                                "type": "array",
                                "items": {"type": "string", "format": "uri"},
                            },
                            "id": {"type": "string"},
                        },
                        "required": ["job_title", "company", "city", "job_link", "id"],
                    },
                },
            },
            "required": ["numFound", "docs"],
        }
    },
    "required": ["response"],
}
