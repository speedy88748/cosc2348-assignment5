#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
assert run(10 + 15).output == "35"
assert run(10 / 5).output == "2"
###

print("All tests passed!")
