# Error Handling API

A FastAPI service that demonstrates how to design and handle
controlled API failures using proper HTTP status codes.

This project focuses on distinguishing between successful
responses and expected failure cases in backend services.

## Endpoint

### GET /items/{item_id}

Returns item data if the item exists.

- If `item_id` is `1`, the item is found
- For any other `item_id`, the API returns `404 Not Found`

Example success response:
```json
{
  "item_id": 1,
  "name": "Example Item"
}
```
Example error response:
```json
{
  "detail": "Item not found"
}
```
Error Handling

Uses HTTPException to explicitly signal failures

Returns correct HTTP status codes

Avoids returning error messages with 200 OK