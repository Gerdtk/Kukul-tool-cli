import sys

from serviceInput.cli_input import CLIInput
from serviceOutput.print_output import PrintOutput
from components.command_processor import CommandProcessor

from components.basic_processor import BasicProcessor
from components.ascii_letter_processor import AsciiLetterProcessor
from components.save_processor import SaveProcesor

from database import InMemoryDB
from core import run

def build_pipeline(option, db=None):
    base = [CommandProcessor(db)]

    if option == "1":
        return base + [AsciiLetterProcessor()]
    elif option == "2":
        return base + [SaveProcesor(db), BasicProcessor()]
    elif option == "3":
        return base + [BasicProcessor(), AsciiLetterProcessor()]
    return base

def main():
    print("[SYSTEM]: ready")

    use_db = "--db" in sys.argv

    input_service = CLIInput()
    output_service = PrintOutput()

    db = InMemoryDB() 
    if use_db:
        print("[MODE]: DB ENABLED...")
    else: None

    

    while True:
        print("\n MENU PRINCIPAL")
        print("1️⃣ - ASCII")
        print("2️⃣ - Básico")
        print("3️⃣ - Pipeline")
        print("0️⃣ - Salir")

        option = input(" Elige Opcion: ")

        if option == "0":
            print("Bye")
            break

        processors = build_pipeline(option, db)

        while True:
            message = input("> ").strip()

            if message.lower() == "exit":
                break

            data = {"message": message}

            for processor in processors:
                data = processor.process(data)
                if data is None:
                    raise ValueError(f"{processor.__class__.__name__} devolvio None")
                if data.get("stop_pipeline"):
                    break

            if "message" in data:
                print(data["message"])
            else: 
                print(data)


if __name__ == "__main__":
    main()