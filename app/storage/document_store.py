class DocumentStore:
    def __init__(self):
        self.store = {}
        self.processed_events = set()

    def save_annotation(self, event_id, image_id, data):
        if event_id in self.processed_events:
            return False

        self.processed_events.add(event_id)
        self.store[image_id] = data
        return True

    def get(self, image_id):
        return self.store.get(image_id)