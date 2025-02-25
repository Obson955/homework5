from calculator.commands.calculator_command import CalculatorCommand

class DivideCommand(CalculatorCommand):
    def __init__(self):
        super().__init__(lambda a, b: a / b)