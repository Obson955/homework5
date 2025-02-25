
from calculator.commands.calculator_command import CalculatorCommand

class AddCommand(CalculatorCommand):
    def __init__(self):
        super().__init__(lambda a, b: a + b)