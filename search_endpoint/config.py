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
endpoint = [
    ("search/", "?query=developer", 200),
    ("search/", "?query=engineer", 200),
    ("search/", "?q= ", 200),
    ("search/", "?query=20", 404),
    ("search/", "?r=manager", 404),
    ("search/", "?ssl=engineer", 404),
    ("searc/", "?query=&", 404),
]

# Define API test cases Error cases
endpoint_tests = [
    ("search/", "?query=backend", 500),  # Internal Server Error
    ("search/", "?query=frontend", 502),  # Bad Gateway
    ("search/", "?query=database", 503),  # Service Unavailable
    ("search/", "?query=bigdata", 507),  # Insufficient Storage
]
