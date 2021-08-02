import pytest
from my_source import add_func

#funktionierende Test
def test_add_one():
    assert add_func(2, 5) == 7

#nicht funktionierende Test
@pytest.mark.xfail
def test_add_fail():
    assert add_func(5, 5) == 9
