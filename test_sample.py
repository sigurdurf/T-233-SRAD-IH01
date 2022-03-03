import pytest
from sample import FizzBuzzError, Fizz_Buzz

def test_one_to_ten():
    Fizz_Buzz_string = Fizz_Buzz(10)
    assert Fizz_Buzz_string == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz"

def test_one_to_fifteen():
    Fizz_Buzz_string = Fizz_Buzz(15)
    assert Fizz_Buzz_string == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"

def test_one_to_hundred():
    Fizz_Buzz_string = Fizz_Buzz(100)
    assert Fizz_Buzz_string == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz"

def test_range_ten():
    Fizz_Buzz_string = Fizz_Buzz(10)
    Fizz_Buzz_length = len(Fizz_Buzz_string.split(" "))
    assert Fizz_Buzz_length == 10

def test_range_negative_10():
    Fizz_Buzz_string = Fizz_Buzz(-10)
    assert Fizz_Buzz_string == None

def test_range_some_string():
    with pytest.raises(FizzBuzzError):
        Fizz_Buzz_string = Fizz_Buzz("Some random input string")
    
def test_range_with_float():
    Fizz_Buzz_string = Fizz_Buzz(37.39283238638603)
    assert Fizz_Buzz_string == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37"
 