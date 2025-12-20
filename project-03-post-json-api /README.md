# POST JSON API

A simple FastAPI service that demonstrates how to receive,
validate, and process JSON request bodies using Pydantic models.

This project focuses on handling structured client input
through HTTP POST requests, which is the most common pattern
for real-world backend APIs.

## Endpoint

### POST /echo

Receives a JSON payload and echoes the validated data back.

Example request body:
```json
{
  "message": "hello backend"
}
Example response:

{
  "message": "hello backend"
}