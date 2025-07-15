# Expense Tracker API

A backend API for tracking personal expenses. Built with FastAPI and PostgreSQL, containerized with Docker, and monitored using Prometheus.

## Features
- Add, update, delete, and filter expenses
- View expense statistics (total, by category)
- Fully dockerized with PostgreSQL and pgAdmin
- Metrics for all routes via Prometheus /metrics endpoint
- CI setup with GitHub Actions


## Tech Stack

- FastAPI, Tortoise ORM, PostgreSQL, Docker + docker-compose, Prometheus, GitHub Actions

---
.ENVs 

POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123321
POSTGRES_DB=expenses

## Prometheus metrics 
GET /metrics

## Prometheus queries via GUI
http_requests_total
expenses_created_total
http_request_duration_seconds
