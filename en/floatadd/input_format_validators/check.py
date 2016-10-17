#!/usr/bin/env python
# Silly sample input format validator.
from sys import stdin
import sys
import re

#float_number = "((0|-?[1-9]\d*)\.[0-9]+)"
float_number = "((0|-?[1-9]\d*)\.[0-9]{1,5})"

line = stdin.readline()
assert re.match(float_number + " " + float_number + "\n", line)

[a, b] = [float(x) for x in line.split()]
assert 0.0 <= a <= 50.0
assert 0.0 <= b <= 50.0

# Check for trailing input
assert len(stdin.readline()) == 0

# Nothing to report
sys.exit(42)
