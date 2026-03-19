from datetime import datetime


class BasicErrorHandler:
    def handle(self, error, data, processor):

        if data is None:
            data = {}
            
        error_info = {
            "Type": type(error).__name__,
            "datetime": datetime.now().isoformat(),
            "where": processor.__class__.__name__,
            "who": data,
        }

        print(f"\n ================================================================ \n")
        print(f"\n Error detectado")
        print(f"Type: {error_info['Type']}")
        print(f"when: {error_info['datetime']}")
        print(f"where: {error_info['where']}")
        print(f"Data: {error_info['who']}")
        print(f"Message: {str(error)}\n")
        print(f"\n ================================================================ \n")


        data["message"] = f"Error en {error_info['where']}"
        data["error"] = error_info

        return data