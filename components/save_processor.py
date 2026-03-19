from contracts import ProcessContract

class SaveProcesor(ProcessContract):
    def __init__(self, db):
        self.db = db
    
    def process(self, data: dict) -> dict:
        self.db.create(data)
        return data
    
