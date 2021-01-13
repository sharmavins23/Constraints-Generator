from abc import ABC, abstractmethod
from .ConstraintLine import ConstraintLine  # Parent class
# Contains object definition on package pin object


class IOStandard(ConstraintLine):
    def __init__(self, busName=None, idx=None):
        super().__init__(busName, idx)

    def __str__(self):
        super().__str__()  # Set property
        self.string += "IOSTANDARD LVCMOS18 "
        self.string += "[get_ports {" + self.busName + "[" + self.idx + "]}]"

        return self.string
