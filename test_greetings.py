#!/usr/bin/env python3
"""Various greetings testing"""

import pytest
from greetings import hello, hi


AUDIENCE = [
    ("World", "Hello, World"),
    ("MICS 2020", "Hello, MICS 2020"),
]


def test_hi():
    """Testing the output of `hi`"""
    assert hi() == "Hi there"


@pytest.mark.parametrize("data, expected", AUDIENCE)
def test_hello(data, expected):
    """Testing the output of `hello`"""
    assert hello(data) == expected


AUDIENCE_ERR = [42, None, [1, 2]]


@pytest.mark.parametrize("data", AUDIENCE_ERR)
def test_hello_err(data):
    """Testing the exception raised by `hello`"""
    with pytest.raises(TypeError) as exc:
        hello(data)
    assert str(exc.value) == "Unable to greet " + str(data)
