
from calculator.app.commands.command_handler import CalculatorCommand

class AddCommand(CalculatorCommand):
    def __init__(self):
        super().__init__(lambda a, b: a + b)