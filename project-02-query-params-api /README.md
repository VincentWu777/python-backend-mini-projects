# Query Params API

A simple FastAPI service that demonstrates how to receive and
validate query parameters from HTTP GET requests.

This project shows how backend services handle client input
through URL query parameters and perform automatic validation.

## Endpoints

### GET /add

Adds two integers provided as query parameters.

Example request:
GET /add?a=3&b=5


Response:
```json
{
  "a": 3,
  "b": 5,
  "result": 8
}