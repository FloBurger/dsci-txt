import pandas
#writefile first.py
def first(l):
    return l[0]

def test_first():
    assert first([1, 2, 3]) == 1