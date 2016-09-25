#!/usr/bin/env python
# Silly sample input format validator.
from sys import stdin
import sys
import re

integer = "(0|-?[1-9]\d*)"

cnt = 0
for line in stdin:
    assert re.match(integer + " " + integer + "\n", line)

    [a, b] = [int(x) for x in line.split()]
    assert 0 <= a <= 10 ** 15
    assert 0 <= b <= 10 ** 15

    cnt += 1

assert 0 < cnt <= 1000

# Nothing to report
sys.exit(42)
