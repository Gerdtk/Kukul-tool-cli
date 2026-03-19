from contracts import OutputContract

class PrintOutput(OutputContract):
    def deliver(self, data: dict) -> None:
        result = data.get("result")

        if isinstance(result, list):
            for line in result:
                print(line)
        else:
            print(result)