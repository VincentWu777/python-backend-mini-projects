# Pagination & Filtering API

A FastAPI service that demonstrates how to design scalable
collection APIs using pagination and filtering.

This project focuses on protecting backend systems from
unbounded data access and providing predictable, controllable
views of resource collections.

## Resource Model

The API works with a Todo resource:

- `id` (int): unique identifier
- `title` (str): task description
- `completed` (bool): task status

## Pagination

The API supports limit/offset pagination via query parameters.

### Parameters

- `limit` (int, default: 10, max: 100)
  - Maximum number of items to return
  - Used as a defensive system constraint

- `offset` (int, default: 0)
  - Number of items to skip before returning results
Example:

GET /todos?limit=2&offset=2


## Filtering

The API supports filtering Todos by completion status.

### Parameters

- `completed` (bool, optional)
  - `true`: return completed Todos
  - `false`: return incomplete Todos
  - omitted: no filtering applied

Example:

GET /todos?completed=false


## Pagination + Filtering

Filtering is applied before pagination.

Example:

GET /todos?completed=true&limit=1&offset=1


This ensures stable and predictable pagination behavior.

## Error Handling

- Invalid query parameters return `422 Unprocessable Entity`
- Input validation is enforced at the API boundary
- The system rejects unbounded or invalid requests


