
from calculator.commands.calculator_command import CalculatorCommand

class SubtractCommand(CalculatorCommand):
    def __init__(self):
        super().__init__(lambda a, b: a - b)