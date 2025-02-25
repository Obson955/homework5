import pytest
from calculator.app import App
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand


def test_add_command(capfd, monkeypatch):
    """Test that the AddCommand correctly adds two numbers."""
    inputs = iter(['5', '10'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    command = AddCommand()
    command.execute()
    
    out, err = capfd.readouterr()
    assert out == "Result: 15\n", "The AddCommand should print the correct result"

def test_subtract_command(capfd, monkeypatch):
    """Test that the SubtractCommand correctly subtracts two numbers."""
    inputs = iter(['10', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    command = SubtractCommand()
    command.execute()
    
    out, err = capfd.readouterr()
    assert out == "Result: 5\n", "The SubtractCommand should print the correct result"

def test_multiply_command(capfd, monkeypatch):
    """Test that the MultiplyCommand correctly multiplies two numbers."""
    inputs = iter(['5', '10'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    command = MultiplyCommand()
    command.execute()
    
    out, err = capfd.readouterr()
    assert out == "Result: 50\n", "The MultiplyCommand should print the correct result"

def test_divide_command(capfd, monkeypatch):
    """Test that the DivideCommand correctly divides two numbers."""
    inputs = iter(['10', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    command = DivideCommand()
    command.execute()
    
    out, err = capfd.readouterr()
    assert out == "Result: 2\n", "The DivideCommand should print the correct result"

def test_menu_command(capfd):
    """Test that the MenuCommand correctly shows the available commands."""
    command = MenuCommand()
    command.execute()
    
    out, err = capfd.readouterr()
    expected_output = """Available commands:
1. greet - Greet the user
2. add - Add two numbers
3. subtract - Subtract two numbers
4. multiply - Multiply two numbers
5. divide - Divide two numbers
6. menu - Show this menu
7. exit - Exit the application"""
    
    assert out.strip() == expected_output.strip(), "The MenuCommand should print the correct menu"

def test_app_add_command(capfd, monkeypatch):
    """Test that the App REPL correctly handles the 'add' command."""
    inputs = iter(['add', '5', '10', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_subtract_command(capfd, monkeypatch):
    """Test that the App REPL correctly handles the 'subtract' command."""
    inputs = iter(['subtract', '10', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_multiply_command(capfd, monkeypatch):
    """Test that the App REPL correctly handles the 'multiply' command."""
    inputs = iter(['multiply', '5', '10', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_divide_command(capfd, monkeypatch):
    """Test that the App REPL correctly handles the 'divide' command."""
    inputs = iter(['divide', '10', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the App REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
