#Make Python Tests
import pytest
import ben_future_value.future_value as bfv

def test_Future_Value():
    future_value = bfv.Future_Value(1000,7,200,40,4)

    assert future_value.Principle_value == 1000