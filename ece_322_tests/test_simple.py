"""Equivalence class based pytests for the pendulum.parse method"""

import pytest

import pendulum
from pendulum.parsing import ParserError


def test_i_16():
    text = "5:33:60"
    with pytest.raises(ValueError):
        pendulum.parse(text)


def test_i_17():
    text = "5:33:-01"
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_18():
    text = "5:33:ab"
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_19():
    text = "02:34:"
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_20():
    text = "5:33:001"
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_21():
    text = "5:60"
    with pytest.raises(ValueError):
        pendulum.parse(text)


def test_i_22():
    text = "5:-01"
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_23():
    text = "5:aa"
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_24():
    text = "01:"
    with pytest.raises(TypeError):  # interestingly this raises a type error
        pendulum.parse(text)


def test_i_25():
    text = "05:001"
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_26():
    text = "24:00"
    with pytest.raises(ValueError):
        pendulum.parse(text)


def test_i_27():
    text = "-1:00"
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_28():
    text = "aa:00"
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_29():
    text = ":00"
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_30():
    text = "001:00"
    with pytest.raises(ParserError):
        pendulum.parse(text)


# 01 is day
# 02 is month
# 2018 is year
@pytest.mark.parametrize("text",
    [
        "2018-02-01",     # dd-mm-yyyy
    ]
)
def test_i_31(text):
    parsed = pendulum.parse(text)

    assert 2018 == parsed.year
    assert 1 == parsed.day
    assert 2 == parsed.month


@pytest.mark.parametrize("text",
    [
        "2018-01-02",
    ]
)
def test_i_31_fail_assert(text):
    parsed = pendulum.parse(text)

    with pytest.raises(AssertionError):
        assert 2018 == parsed.year
        assert 1 == parsed.day
        assert 2 == parsed.month


@pytest.mark.parametrize("text",
    [
        "02-2018-01",
        "01-2018-02",
        "02-01-2018",
        "01-02-2018"
    ]
)
def test_i_31_fail_parse(text):
    with pytest.raises(ParserError):
        pendulum.parse(text)


def test_i_32():
    text = ""
    with pytest.raises(ValueError):
        pendulum.parse(text)
