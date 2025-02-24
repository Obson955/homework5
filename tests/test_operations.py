"""Test suite for calculator operations."""

from decimal import Decimal
import pytest

from calculator.operations import add, subtract, multiply, divide

def test_add():
    """Test addition of two decimal numbers."""
    assert add(Decimal('1.1'), Decimal('2.2')) == Decimal('3.3')

def test_subtract():
    """Test subtraction of two decimal numbers."""
    assert subtract(Decimal('5.5'), Decimal('2.2')) == Decimal('3.3')

def test_multiply():
    """Test multiplication of two decimal numbers."""
    assert multiply(Decimal('2.0'), Decimal('3.5')) == Decimal('7.0')

def test_divide():
    """Test division of two decimal numbers."""
    assert divide(Decimal('7.0'), Decimal('2.0')) == Decimal('3.5')

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(Decimal('1.0'), Decimal('0.0'))
