#!/usr/bin/env python
# Silly sample input format validator.
from sys import stdin
import sys
import re

integer = "(0|-?[1-9]\d*)"

line = stdin.readline()
assert re.match(integer + " " + integer + "\n", line)

[a, b] = [int(x) for x in line.split()]
assert 0 <= a <= 2 ** 31 - 1
assert 0 <= b <= 2 ** 31 - 1

# Check for trailing input
assert len(stdin.readline()) == 0

# Nothing to report
sys.exit(42)
