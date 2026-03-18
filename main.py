from serviceInput.cli_input import CLIInput
from components.basic_processor import BasicProcessor
from serviceOutput.print_output import PrintOutput
from core import run 



def main():
    print("[SYSTEM]: ready")

    input_service = CLIInput()
    processor = BasicProcessor()
    output_service = PrintOutput()

    while True:
        run(
            input_service=input_service,
            processor=processor,
            output_service=output_service,
        )
        if data["message"].lower() == 'exit':
            print("Bye")
            exit()

if __name__ == "__main__":
    main()