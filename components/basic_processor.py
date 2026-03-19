from contracts import ProcessContract

class BasicProcessor(ProcessContract):
    def __init__(self, db=None):
        self.db = db


    def process(self, data: dict) -> dict:
        message = data["message"]

        if self.db and not message.startswith("/"):
            self.db.save(message)
            print(f"Guardado: {message}")



        data["result"] = message
        data["message"] = message
        
        return data
