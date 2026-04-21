# Event-Driven Image Annotation and Retrieval System

## Overview
This project implements an event-driven architecture for an image annotation and retrieval system. The goal is to demonstrate system design principles such as decoupling, scalability, and fault tolerance, rather than building a machine learning model.

---

## System Architecture
The system is composed of independent services that communicate through events using a publish-subscribe model:

- CLI Service: Publishes image.submitted  
- Inference Service: Processes images and publishes inference.completed  
- Annotation Service: Stores results and publishes annotation.stored  
- Query Service: Handles retrieval requests  

Each service operates independently and does not directly access other services' data.

---

## Event Flow
The system follows a sequential event pipeline:

1. image.submitted → triggered by CLI  
2. inference.completed → produced by inference service  
3. annotation.stored → produced by annotation service  
4. Query service retrieves stored results  

Each event contains:
- event_id (unique identifier)  
- timestamp  
- payload (data content)  

---

## Data Storage
A simple in-memory document store is implemented:

- Stores annotations indexed by image_id  
- Uses a flexible JSON-like structure  
- Simulates a NoSQL/document database  

Example structure:

{  
  "image_id": "img_001",  
  "objects": ["cat", "dog"]  
}  

---

## Idempotency
The system ensures duplicate events do not create duplicate state.

This is implemented using:
- A processed_events set  
- Tracking of event_id  

If an event is processed more than once, it is ignored.

---

## Testing
The system includes unit tests covering:

- Event schema validation  
- Malformed events handling  
- Broker behavior (mocked Redis)  
- Idempotency (duplicate event handling)  

All tests pass successfully.

---

## Design Principles
The system is designed with the following principles:

- Event-driven architecture  
- Loose coupling between services  
- Single ownership of data  
- Testability with mocks  
- Fault tolerance (duplicate events handled)  

---

## Limitations
This project does not include:

- Real machine learning inference  
- Vector similarity search  
- Persistent database (in-memory only)  

The focus is on system design rather than AI modeling.

---

## Future Improvements
Potential extensions include:

- Integrating a real database (e.g., MongoDB)  
- Adding embedding and vector search (e.g., FAISS)  
- Implementing asynchronous processing  
- Adding failure injection and retry mechanisms  



