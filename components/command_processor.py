


class CommandProcessor:
    def __init__(self, db=None):
        self.db = db

    def process(self, data: dict) -> dict:
        message = data["message"].strip()

        if not message.startswith("/"):
            return data
        
        if message == "/show_db":
            if self.db is None:
                return {
                    **data,
                    "message": "[DB DISABLED]",
                    "stop_pipeline": True,
                }
            
            if not self.db.storage:
                return {
                    **data,
                    "message": "[DB CONTENT]\n(vacia)",
                    "stop_pipeline": True
                }
            
            lines = ["[DB CONTENT]"]
            for i, item in enumerate(self.db.storage, start=1):
                lines.append(f"{i}, {item}")

            return {
                **data,
                "message": "\n".join(lines),
                "stop_pipeline": True,
            }
        
        return{
            **data,
            "message": f"[UNKNOWN COMMAND] {message}",
            "stop_pipeline": True,
        }