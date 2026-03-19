from contracts import OutputContract

class PrintOutput(OutputContract):
    def deliver(self, data: dict) -> None:
        message = data.get("message")

        if isinstance(message, list):
            for line in message:
                print(line)
        else:
            print(message)