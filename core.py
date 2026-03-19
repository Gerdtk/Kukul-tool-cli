def run(data, processors, error_handler=None):
    for processor in processors:
        try:
            data = processor.process(data)

            if data is None:
                raise ValueError(
                    f"{processor.__class__.__name__} devolvio None"
                )
            if data.get("stop_pipeline"):
                break
        except Exception as e:
            if error_handler:
                data = error_handler.handle(e, data, processor)
            else:
                raise
    return data
    