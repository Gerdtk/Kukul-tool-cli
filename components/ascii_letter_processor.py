from contracts import ProcessContract

class AsciiLetterProcessor(ProcessContract):

    def process(self, data: dict) -> dict:
        message = data["message"].strip().upper()

        letters = {
            "H": [
                "H     H",
                "H     H",
                "HHHHHHH",
                "H     H",
                "H     H",
            ],
            "E": [
                "EEEEEEE",
                "E      ",
                "EEEEE  ",
                "E      ",
                "EEEEEEE",
            ],
            "Y": [
                "Y     Y",
                " Y   Y ",
                "  Y Y  ",
                "   Y   ",
                "   Y   ",
            ]
        }

        output_lines = [""] * 5

        for char in message:
            grid = letters.get(char, ["?"] * 5)

            for i in range(5):
                output_lines[i] += grid[i] + "  "

        data["message"] = "\n".join(output_lines)
        return data 