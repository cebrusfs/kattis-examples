#!/usr/bin/env python
# Silly sample input format validator.
from sys import stdin
import sys
import re

integer = "(0|-?[1-9]\d*)"

line = stdin.readline()
assert re.match(integer + "\n", line)

x = int(line)
assert 0 <= x <= 2000

# Check for trailing input
assert len(stdin.readline()) == 0

# Nothing to report
sys.exit(42)
