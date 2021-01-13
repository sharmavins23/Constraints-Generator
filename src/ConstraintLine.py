from abc import ABC, abstractmethod
# Contains object definition on constraint lines


class ConstraintLine(ABC):
    def __init__(self, busName=None, idx=None):
        self.busName = busName
        self.idx = str(idx)
        self.string = ""

    @abstractmethod
    def __str__(self):
        self.string += "set_property "
        # Rest to be implemented in child classes
