from contracts import InputContract

class CLIInput(InputContract):
    def get_input(self) -> dict:
        user_input = input("> ")
        return {"message": user_input}