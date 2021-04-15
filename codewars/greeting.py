# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

# Use conditionals to return the proper message:

# case	return
# name equals owner	'Hello boss'
# otherwise	'Hello guest'

def greet(name, owner):
    if name == owner: return 'Hello boss'
    else: return 'Hello guest'

def apple(x):
    print(10**2)
    return 'Hotter than the sun!!' if x**2 > 1000 else 'Help yourself to a honeycomb Yorkie for the glovebox.'


def strtonum(x):
    x = list(x)
    for num in x:
        print(num)
        if int(num) > 2: x[int(num.index)] = f"{0}"
    print(x)

strtonum("123")
