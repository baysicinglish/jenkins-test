from script import Greeting
import pytest

def test_returns_input():
    assert Greeting.greet('Dan') == 'Hello, Dan'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        Greeting.greet(9)

test_returns_input()
test_raises_exception_on_non_string_arguments()
