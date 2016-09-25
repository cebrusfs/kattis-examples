#!/usr/bin/env python
# Silly sample input format validator.
from sys import stdin
import sys

# There shouldn't be any input
line = stdin.read()
assert line == ''

# Nothing to report
sys.exit(42)
