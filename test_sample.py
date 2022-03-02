import pytest
from sample import fizz_buzz

def test_one_to_ten():
    fizz_buzz_string = fizz_buzz(10)
    assert fizz_buzz_string == "1 2 fizz 4 buzz fizz 7 8 fizz buzz"

def test_range():
    fizz_buzz_string = fizz_buzz(10)
    fizz_buzz_length = len(fizz_buzz_string.split(" "))
    assert fizz_buzz_length == 10