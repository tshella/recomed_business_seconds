from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_valid_range():
    r = client.get("/business-seconds?start_time=2023-07-10T09:00:00&end_time=2023-07-10T10:00:00")
    assert r.status_code == 200
    assert r.text == "3600"

def test_weekend():
    r = client.get("/business-seconds?start_time=2023-07-08T09:00:00&end_time=2023-07-09T17:00:00")
    assert r.text == "0"

def test_invalid_date():
    r = client.get("/business-seconds?start_time=bad&end_time=also_bad")
    assert r.status_code == 400
