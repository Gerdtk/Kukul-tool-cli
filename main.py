import sys

from serviceInput.cli_input import CLIInput
from serviceOutput.print_output import PrintOutput
from database import InMemoryDB

from pipelines import PIPELINES
from core import run
from error_handlers.basic_capture_errors import BasicErrorHandler


# Estructura basica ejecuta con... / Basic structure starts with...
# main.py



def main():
    print("[SYSTEM]: ready")

    handler = BasicErrorHandler()

    use_db = "--db" in sys.argv

    input_service = CLIInput()
    output_service = PrintOutput()

    db = InMemoryDB() 

    if use_db:
        print("[MODE]: DB ENABLED...")
    else: None

    

    while True:
        print("\n MENU PRINCIPAL")
        print("1 - Basic")
        print("2 - ASCII")
        print("3 - Pipeline")
        print("0 - Salir")

        option = input(" Elige Opcion: ")

        if option == "0":
            print("Bye")
            break

        pipeline_func = PIPELINES.get(option)

        if not pipeline_func:
            print("Opcion Invalida")
            continue

        processors = pipeline_func()

        while True:
            message = input("> ").strip()

            if message.lower() == "exit":
                break
            data = {"message": message}
            result = run(data, processors, error_handler=handler)
            output_service.deliver(result)


if __name__ == "__main__":
    main()