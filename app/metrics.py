import time

from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "http_requests_total", "Total HTTP requests", ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds", "HTTP request latency", ["endpoint"]
)

EXPENSES_CREATED = Counter("expenses_created_total", "Number of expenses created")
