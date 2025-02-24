"""Unit tests for the Calculations class."""

from decimal import Decimal
import pytest

from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add

@pytest.fixture(autouse=True)
def setup_method():
    """Fixture to clear calculation history before each test."""
    Calculations.clear_history()
    yield
    Calculations.clear_history()

def test_add_calculation():
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('1.0'), Decimal('2.0'), add)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1

def test_clear_history():
    """Test clearing the calculation history."""
    calc = Calculation(Decimal('1.0'), Decimal('2.0'), add)
    Calculations.add_calculation(calc)
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

def test_get_latest():
    """Test retrieving the latest calculation from history."""
    calc1 = Calculation(Decimal('1.0'), Decimal('2.0'), add)
    calc2 = Calculation(Decimal('3.0'), Decimal('4.0'), add)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    latest = Calculations.get_latest()
    assert latest is calc2
