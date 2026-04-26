def add_and_maybe_multiply(a, b, c=None):
    result = a + b
    if c is not None:
        result = result * c

    return result
var = add_and_maybe_multiply
print(var)