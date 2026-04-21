# Event-Driven Image Annotation System

## Overview

This project implements an **event-driven image processing pipeline** using Redis as a message broker.

The system processes an image through three stages:

1. Image submission (CLI)
2. Image inference
3. Annotation storage

---

## Architecture

```
CLI Service → image.submitted
    ↓
Inference Service → inference.completed
    ↓
Annotation Service → annotation.stored
```

---

## Components

### 1. CLI Service

* Publishes `image.submitted`
* Contains image ID and file path

### 2. Inference Service

* Subscribes to `image.submitted`
* Simulates object detection
* Publishes `inference.completed`

### 3. Annotation Service

* Subscribes to `inference.completed`
* Stores annotation results
* Publishes `annotation.stored`

---

## Technologies

* Python 3
* Redis (Pub/Sub)
* Virtual Environment (venv)
* Event-driven architecture

---

## Project Structure

```
event-driven-image-system/
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
├── images/
│   └── test1.jpg
└── README.md
```

---

## Setup

```bash
git clone https://github.com/haha-gongzi/event-driven-image-system.git
cd event-driven-image-system
python3 -m venv venv
source venv/bin/activate
pip install redis
```

---

## Start Redis

```bash
sudo service redis-server start
```

---

## Run

Open 3 terminals:

### Terminal 1

```bash
PYTHONPATH=. python app/services/inference_service.py
```

### Terminal 2

```bash
PYTHONPATH=. python app/services/annotation_service.py
```

### Terminal 3

```bash
PYTHONPATH=. python app/services/cli_service.py
```

---

## Example Output

```
Published image.submitted for img_001
Processed image img_001 → inference.completed
Stored annotation for img_001
```

---


