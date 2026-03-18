from contracts import OutputContract

class PrintOutput(OutputContract):
    def deliver(self, data: dict) -> None:
        print(data.get("result"))
        