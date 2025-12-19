# Health Check API

A minimal FastAPI service that exposes health check endpoints
used to verify service availability and version information.

This type of API is commonly used by monitoring systems,
load balancers, and engineers to confirm that a backend service
is running correctly.

## Endpoints

### GET /health
Returns the current health status of the service.

Response:
```json
{
  "status": "ok"
}
