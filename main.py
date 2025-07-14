from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import PlainTextResponse
from business_seconds import calculate_business_seconds
from datetime import datetime

app = FastAPI()

@app.get("/business-seconds", response_class=PlainTextResponse)
def get_business_seconds(
    start_time: str = Query(..., description="Start time in ISO-8601 format"),
    end_time: str = Query(..., description="End time in ISO-8601 format")
):
    try:
        start = datetime.fromisoformat(start_time)
        end = datetime.fromisoformat(end_time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ISO-8601 date format")

    if start >= end:
        raise HTTPException(status_code=400, detail="start_time must be before end_time")

    seconds = calculate_business_seconds(start, end)
    return str(seconds)
