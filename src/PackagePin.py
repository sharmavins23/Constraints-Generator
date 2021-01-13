from abc import ABC, abstractmethod
from .ConstraintLine import ConstraintLine  # Parent class
# Contains object definition on package pin object


class PackagePin(ConstraintLine):
    def __init__(self, busName=None, pin=None, idx=None):
        super().__init__(busName, idx)
        self.pin = pin

    def __str__(self):
        super().__str__()  # Set property
        self.string += "PACKAGE_PIN " + self.pin + " "
        self.string += "[get_ports {" + self.busName + "[" + self.idx + "]}]"

        return self.string
