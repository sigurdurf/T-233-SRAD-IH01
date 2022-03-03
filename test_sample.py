import pytest
from sample import FizzBuzzError, fizz_buzz

def test_one_to_ten():
    fizz_buzz_string = fizz_buzz(10)
    assert fizz_buzz_string == "1 2 fizz 4 buzz fizz 7 8 fizz buzz"

def test_one_to_fifteen():
    fizz_buzz_string = fizz_buzz(15)
    assert fizz_buzz_string == "1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz"

def test_one_to_hundred():
    fizz_buzz_string = fizz_buzz(100)
    assert fizz_buzz_string == "1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz fizz 22 23 fizz buzz 26 fizz 28 29 fizzbuzz 31 32 fizz 34 buzz fizz 37 38 fizz buzz 41 fizz 43 44 fizzbuzz 46 47 fizz 49 buzz fizz 52 53 fizz buzz 56 fizz 58 59 fizzbuzz 61 62 fizz 64 buzz fizz 67 68 fizz buzz 71 fizz 73 74 fizzbuzz 76 77 fizz 79 buzz fizz 82 83 fizz buzz 86 fizz 88 89 fizzbuzz 91 92 fizz 94 buzz fizz 97 98 fizz buzz"

def test_range_ten():
    fizz_buzz_string = fizz_buzz(10)
    fizz_buzz_length = len(fizz_buzz_string.split(" "))
    assert fizz_buzz_length == 10

def test_range_negative_10():
    fizz_buzz_string = fizz_buzz(-10)
    assert fizz_buzz_string == None

def test_range_some_string():
    with pytest.raises(FizzBuzzError):
        fizz_buzz_string = fizz_buzz("Some random input string")
    
def test_range_with_float():
    fizz_buzz_string = fizz_buzz(37.39283238638603)
    assert fizz_buzz_string == "1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz fizz 22 23 fizz buzz 26 fizz 28 29 fizzbuzz 31 32 fizz 34 buzz fizz 37"
    