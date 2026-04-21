# Event-Driven Image Annotation and Retrieval System

## Overview

This project implements an event-driven architecture for an image annotation and retrieval system. The system focuses on modular design, loose coupling, and testability rather than machine learning performance.

The system uses a publish-subscribe model where services communicate via events instead of direct function calls. This improves scalability, maintainability, and extensibility.

---

## System Architecture

The system is composed of independent services:

* **CLI Service** → publishes `image.submitted`
* **Inference Service** → processes images and publishes `inference.completed`
* **Annotation Service** → stores results and publishes `annotation.stored`
* **Query Service** → retrieves stored data and publishes `query.completed`

Each service is loosely coupled and communicates only through events.

---

## Project Structure

```
app/
  broker/        # Message broker abstraction (Redis)
  events/        # Event schemas and topics
  services/      # Core services (CLI, inference, annotation, query)
  storage/       # Document store (in-memory)

tests/
  test_broker.py
  test_event_schema.py
  test_idempotency.py
  test_malformed_events.py
  test_query.py
```

---

## Event Flow

### Annotation Pipeline

```
image.submitted → inference.completed → annotation.stored
```

### Query Pipeline

```
query.submitted → query.completed
```

---

## Event Schema Example

Each event follows a structured format:

```json
{
  "type": "event",
  "topic": "inference.completed",
  "event_id": "evt_123",
  "timestamp": "2026-04-21T12:00:00Z",
  "payload": {
    "image_id": "img_001",
    "objects": ["cat", "dog"]
  }
}
```

---

## Data Storage

The system uses an in-memory document store to simulate a document-oriented database.

* Data is stored by `image_id`
* Supports flexible JSON-like schema
* Allows nested and evolving structures

Example:

```json
{
  "image_id": "img_001",
  "objects": ["cat", "dog"]
}
```

---

## Idempotency

The system prevents duplicate writes from repeated events.

This is implemented using:

* `processed_events` set
* `event_id` tracking

If a duplicate event is received, it is ignored.

---

## Validation

Incoming events are validated before processing.

Validation includes:

* Required fields check
* Topic verification
* Event type validation
* Payload structure validation

Malformed events are safely ignored.

---

## Testing

The project includes unit tests covering:

* Event schema correctness
* Malformed event handling
* Broker behavior
* Idempotency logic

Run tests:

```
python -m pytest -q
```

---

## Quick Start

Install dependencies:

```
pip install -r requirements.txt
```

Run tests:

```
python -m pytest -q
```

---

## Design Principles

* Event-driven architecture
* Loose coupling between services
* Single source of truth for annotation storage
* High testability via unit tests
* Fault tolerance through validation and idempotency

---

## Limitations

* No real ML model (simulated inference)
* In-memory storage (non-persistent)
* No distributed deployment
* No retry mechanism

---

## Future Improvements

* Replace in-memory store with MongoDB
* Add embedding-based retrieval
* Integrate vector search (FAISS)
* Add retry queues and failure handling
* Extend query pipeline for semantic search

