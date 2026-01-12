import pytest

from seminar_project.simple import add_one

def test_add_one():
    assert add_one(5) ==  6