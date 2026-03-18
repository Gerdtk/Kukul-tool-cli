from contracts import ProcessContract

class BasicProcessor(ProcessContract):
    def process(self, data: dict) -> dict:
        if "message" not in data:
            raise ValueError("missing 'message'")
        
        return {"result": data["message"]}
    
