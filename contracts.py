from abc import ABC, abstractmethod

class InputContract(ABC):
    @abstractmethod
    def get_input(self) -> dict:
        pass

class ProcessContract(ABC):
    @abstractmethod
    def process(self, data: dict) -> dict:
        pass

class OutputContract(ABC):
    def deliver(self, data: dict) -> None:
        pass
