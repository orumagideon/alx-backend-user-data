# Simple-basic-API

## Setup and Start

1. Download and start your project from this [archive.zip]

2. Install dependencies:
pip3 install -r requirements.txt

markdown

3. Start the server:
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app

shell

## Testing the API

In another tab or in your browser, you can use curl to interact with the API:

### Check API Status

curl "http://0.0.0.0:5000/api/v1/status" -vvv

bash

### Error Handler: Unauthorized

- Route: GET /api/v1/unauthorized

curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv

bash

### Error Handler: Forbidden

- Route: GET /api/v1/forbidden

curl "http://0.0.0.0:5000/api/v1/forbidden" -vvv
