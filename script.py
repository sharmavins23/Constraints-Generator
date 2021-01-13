from src.ConstraintLine import ConstraintLine
from src.PackagePin import PackagePin
from src.IOStandard import IOStandard


# Create the PACKAGE_PIN TCL line
def createPackagePinConstraint(busName, pin, idx):
    line = PackagePin(busName=busName, pin=pin, idx=idx)
    return line


# Create the IOSTANDARD TCL line
def createIOStandardConstraint(busName, idx):
    line = IOStandard(busName=busName, idx=idx)
    return line


# Driver code
if __name__ == "__main__":
    # Input bus name
    busName = input("Please enter the name of the constraint bus. ")

    pinList = []
    print("Please enter the pins, starting from index 0.")
    print("When finished, enter 0x0.")
    while True:
        pin = input("> ")
        if pin == "0x0":
            break
        else:
            pinList.append(pin)

    print()  # Whitespace

    for idx, pin in enumerate(pinList):
        print(createPackagePinConstraint(busName, pin, idx))
        print(createIOStandardConstraint(busName, idx))
