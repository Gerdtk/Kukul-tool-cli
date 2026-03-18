def run(input_service, processor, output_service):
    data = input_service.get_input()
    result = processor.process(data)
    output_service.deliver(result)
