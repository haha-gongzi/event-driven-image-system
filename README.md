# Event-Driven Image Annotation System

## Overview
This project implements an event-driven image annotation system using a publish-subscribe architecture. The goal is to demonstrate system design principles rather than machine learning.

---

## Architecture

The system consists of loosely coupled services:

- CLI Service → publishes image.submitted
- Inference Service → processes and publishes inference.completed
- Annotation Service → stores results and publishes annotation.stored
- Query Service → handles retrieval requests

Services communicate only via events.

---

## Event Flow

image.submitted → inference.completed → annotation.stored

Each event contains:
- event_id
- timestamp
- payload

---

## Data Storage

A simple in-memory document store is used:

- Stores annotations by image_id
- Supports flexible JSON-like structure

---

## Idempotency

Duplicate events are handled using:

- processed_events set
- event_id tracking

If an event is processed more than once, it is ignored.

---

## Testing

The system includes tests for:

- Event schema validation
- Malformed events
- Broker behavior (mocked)
- Idempotency

All tests pass successfully.

---

## Design Principles

- Event-driven architecture
- Loose coupling
- Single ownership of data
- Testability
- Fault tolerance

---

## Future Work

- Vector search (FAISS)
- Embedding service
- Real database integration

