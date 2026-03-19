def run(input_service, processors, output_service):
    data = input_service.get_input()

    for processor in processors:
     data = processor.process(data)

    output_service.deliver(data)

    return data
