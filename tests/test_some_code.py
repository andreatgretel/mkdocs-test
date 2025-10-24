from test.some_code import SomeClass

def test_sum():
    some_class = SomeClass(x=1)
    assert some_class.some_method(y=2) == 3
