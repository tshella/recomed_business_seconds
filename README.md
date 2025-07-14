# RecoMed Business Seconds API

A Python-based REST API that calculates the number of **business seconds** between two ISO-8601 timestamps. Business seconds are defined as seconds between `08:00` and `17:00` on weekdays (Mon–Fri), **excluding** South African public holidays.

---

**Author: Manaka Anthony Raphasha**

---
## Specification

**Endpoint:** `GET /business-seconds`

### Query Parameters

| Name        | Type   | Format      | Description                          |
|-------------|--------|-------------|--------------------------------------|
| `start_time`| string | ISO-8601    | Start datetime (e.g. `2023-07-10T09:00:00`) |
| `end_time`  | string | ISO-8601    | End datetime (must be after `start_time`)   |

### Example

GET /business-seconds?start_time=2023-07-10T09:00:00&end_time=2023-07-10T17:00:00

Response:
    28800

## Tech Stack

- Python 3.11

- FastAPI

- Docker

- pytest for testing

## Setup & Run

    git clone https://github.com/tshella/recomed_business_seconds
    cd recomed_business_seconds

## Run locally (Dev)
 
    make setup     # (once)
    make run       # start API
    make test      # run tests
    make format    # auto-format
    make lint      # check style
    make docker-build && make docker-run  # container mode

Or manually:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt -r requirements-dev.txt
    python -m uvicorn main:app --reload


API will be available at: http://127.0.0.1:8000/business-seconds

## Run Tests

    make test

## Docker Deployment

### Build & Run via Docker

    ./deploy.sh

Or manually:

    docker build -t recomed-api .
    docker run -p 8000:8000 recomed-api

## Public Holiday Logic

The public holiday calendar is hardcoded in holidays_za.py for simplicity. You may update or extend it based on:

- Official SA Government Calendar
- Or integrate with a custom calendar service

## Features

- ISO-8601 datetime input parsing

- Excludes weekends and SA public holidays

- Pure Python (no 3rd-party holiday packages)

- Dockerized for production

- Fully tested via pytest

## Example Test Cases

| Start                       | End                         | Expected Seconds     |
| --------------------------- | --------------------------- | -------------------- |
| `2023-07-10T09:00:00`       | `2023-07-10T10:00:00`       | 3600                 |
| `2023-07-08T09:00:00` (Sat) | `2023-07-09T17:00:00` (Sun) | 0                    |
| `2023-12-25T08:00:00`       | `2023-12-25T17:00:00`       | 0 *(Public Holiday)* |

## License

MIT License – feel free to use and modify for assessment purposes