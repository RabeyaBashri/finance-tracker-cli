from abc import ABC, abstractmethod

class FileManager(ABC) :

    @abstractmethod
    def load():
        pass

    @abstractmethod
    def save():
        pass   

