from contracts import DBContract

class InMemoryDB(DBContract):

    def __init__(self):
        self.storage = []

    def create(self, data):
        self.storage.append(data)

    def read(self, query):
        return self.storage
    
    def update(self, query, data):
        pass

    def delete(self, query):
        pass

    