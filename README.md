# Event-Driven Image Annotation and Retrieval System

## Overview
This project implements an event-driven architecture for an image annotation and retrieval system. The system focuses on modular design, loose coupling, and testability rather than machine learning performance.

The project uses a publish-subscribe model in which services communicate through events instead of calling each other directly. This makes the system easier to extend, test, and reason about.

---

## System Architecture
The system is composed of independent services:

- **CLI Service**: publishes `image.submitted`
- **Inference Service**: listens for submitted images and publishes `inference.completed`
- **Annotation Service**: stores annotation results and publishes `annotation.stored`
- **Query Service**: handles retrieval requests and publishes `query.completed`

Each service operates independently and communicates only through events.

---

## Event Flow
The main event pipeline is:

1. `image.submitted`
2. `inference.completed`
3. `annotation.stored`

The query path is:

1. `query.submitted`
2. `query.completed`

Each event contains:
- `type`
- `topic`
- `event_id`
- `timestamp`
- `payload`

---

## Data Storage
The project includes a simple in-memory document store that simulates a document-oriented database.

It stores annotations by `image_id` and supports flexible JSON-like records. This design is easier to evolve than a rigid relational schema because different images may contain different objects and nested annotation fields.

Example record:

{
  "image_id": "img_001",
  "objects": ["cat", "dog"]
}

---

## Idempotency
The system is designed so that duplicate events do not create duplicate state.

This is implemented using:
- a `processed_events` set
- `event_id` tracking inside the document store

If the same event is received more than once, it is ignored instead of being written again.

---

## Validation
Incoming events are validated before processing.

The validator checks:
- required fields
- valid topic names
- correct event type
- correct payload type

Malformed events are ignored instead of crashing the service.

---

## Testing
The project includes unit tests for:

- event schema creation
- malformed event handling
- broker publishing behavior
- idempotency for duplicate events

These tests verify the architecture and message contracts, not just the implementation details.

---

## Design Principles
This project follows several core software engineering principles:

- **Event-driven architecture** for decoupled services
- **Loose coupling** between components
- **Single ownership of data** in the annotation storage layer
- **Testability** through mocks and isolated unit tests
- **Fault tolerance** through validation and duplicate-event handling

---

## Limitations
This project does not currently include:

- real machine learning inference
- persistent database storage
- vector similarity search
- retry queues or distributed deployment

The main goal is to demonstrate architecture, messaging, and system behavior.

---

## Future Improvements
Possible extensions include:

- integrating a real document database such as MongoDB
- adding an embedding service
- integrating vector search such as FAISS
- adding retry and failure-injection testing
- extending the query pipeline for semantic retrieval

---

## Requirements
Install dependencies with:

`pip install -r requirements.txt`

Run tests with:

`python -m pytest -q`


