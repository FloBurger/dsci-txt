def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    else:
        return False

def is_divideby(number, a, b):
    return number % a == 0 and number % b == 0

print(is_divide_by(12,-3,4))