from contracts import ProcessContract

class AsciiLetterProcessor(ProcessContract):
    def process(self, data: dict) -> dict:
        #extraer la aletra del input

        char = data["message"].strip().upper()

        #Diccionario de letras en ASCII grid 
        letter = {
            "H": [
                "H     H",
                "H     H",
                "HHHHHHH",
                "H     H",
                "H     H", 
            ]
        }

        #obtener el grid o el Error message
        result = letter.get(char, ["Letra no soportada"])

        #retornar salida 
        return {
            **data,
            "message": "\n".join(result)
        }