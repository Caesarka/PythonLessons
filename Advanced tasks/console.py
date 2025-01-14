#1. Contract

from abc import ABC, abstractmethod

class ConsoleInterface(ABC):
    @abstractmethod
    def print(self, value):
        pass

    @abstractmethod
    def input(self):
        pass

#2. Real Implementation
class RealConsole(ConsoleInterface):
    def print(self, value):
        print(value)

    def input(self):
        return input()
