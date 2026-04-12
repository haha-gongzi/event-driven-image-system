Event-Driven Image Annotation System
Overview

This project implements an event-driven image processing pipeline using Redis as a message broker.
The system demonstrates how multiple services can communicate asynchronously through events, improving scalability and decoupling.

The pipeline processes an image through three stages:

Image submission (CLI)
Image inference (mock model)
Annotation storage
System Architecture

The system follows an event-driven architecture:

CLI Service → image.submitted
→ Inference Service → inference.completed
→ Annotation Service → annotation.stored

Each service listens to specific events and publishes new events after processing.

Components
1. CLI Service
Entry point of the system
Publishes image.submitted event
Includes image ID and file path
2. Inference Service
Subscribes to image.submitted
Simulates object detection
Publishes inference.completed event with detected objects
3. Annotation Service
Subscribes to inference.completed
Stores annotation results (simulated)
Publishes annotation.stored event
Technologies Used
Python 3
Redis (Pub/Sub messaging)
Virtual Environment (venv)
Event-driven architecture design
Project Structure

event-driven-image-system/
│
├── app/
│   ├── broker/
│   │   └── redis_broker.py
│   ├── events/
│   │   ├── schemas.py
│   │   ├── topics.py
│   │   └── validators.py
│   └── services/
│       ├── cli_service.py
│       ├── inference_service.py
│       └── annotation_service.py
│
├── images/
│   └── test1.jpg
│
└── README.md

Setup Instructions
1. Clone the Repository
git clone https://github.com/haha-gongzi/event-driven-image-system.git
cd event-driven-image-system
2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install redis
4. Start Redis Server
sudo service redis-server start
How to Run

Open three terminals:

Terminal 1 – Inference Service
source venv/bin/activate
PYTHONPATH=. python app/services/inference_service.py
Terminal 2 – Annotation Service
source venv/bin/activate
PYTHONPATH=. python app/services/annotation_service.py
Terminal 3 – CLI Service
source venv/bin/activate
PYTHONPATH=. python app/services/cli_service.py
Example Output
CLI
Published image.submitted for img_001
Inference Service
Received event: {...}
Processed image img_001 → inference.completed
Annotation Service
Annotation service received: {...}
Stored annotation for img_001
Key Features
Asynchronous communication using Redis Pub/Sub
Decoupled microservice-style architecture
Event validation for robustness
Easy to extend with real ML models
Design Advantages
Loose coupling between services
Scalable and modular design
Easy to add new services or event types
Clear separation of responsibilities
Future Improvements
Replace mock inference with real ML model (e.g., CNN)
Store annotations in a database
Add REST API layer
Implement message queue (e.g., Kafka)
