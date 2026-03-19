from components.basic_processor import BasicProcessor
from components.ascii_letter_processor import AsciiLetterProcessor
from components.command_processor import CommandProcessor
from components.save_processor import SaveProcesor

def create_basic_pipeline():
    return [
        CommandProcessor(),
        BasicProcessor(),
    ]

def create_ascii_pipeline():
    return [
        CommandProcessor(),
        AsciiLetterProcessor(),

    ]

def create_full_pipeline(save=False):
    processors = [
        CommandProcessor(),
        BasicProcessor(),
        AsciiLetterProcessor(),
    ]

    if save:
        processors.append(SaveProcesor())
    
    return processors

def create_save_pipeline():
    return [
        CommandProcessor(),
        BasicProcessor(),
        SaveProcesor(),
    ]

PIPELINES = {
    "1": create_basic_pipeline,
    "2": create_ascii_pipeline,
    "3": create_full_pipeline,
    "4": create_save_pipeline,
}