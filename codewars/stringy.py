def stringy(size):
    str = ""
    if size == 1:
        return '1'
    if size % 2 == 0:
        str = "10" * int(size/2)
    else:
        str = "10" * int(size/2) + "1"
    return str

def stringy1(size):
    return ('10' * size)[:size]

print(stringy1(4))
