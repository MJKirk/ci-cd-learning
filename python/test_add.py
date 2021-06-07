import pytest
import add

def test_add():
    assert add.myadd(1,2) == 3

def test_fail():
    with pytest.raises(ValueError):
      add.myadd("hello", "world")
 
