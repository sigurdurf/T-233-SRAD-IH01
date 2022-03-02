
def fizz_buzz(r):
    if r < 1:
        return None
    result = []
    for x in range(1, r+1):
        fizz_str = ""
        if x % 3 == 0:
            fizz_str += "fizz"
        if x % 5 == 0:
            fizz_str += "buzz"
        if len(fizz_str) == 0:
            fizz_str += str(x)
        result.append(fizz_str)
    return " ".join(result)