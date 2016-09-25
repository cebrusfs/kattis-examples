#!/usr/bin/env python

# ./validator input judge_answer feedback_dir [additional_arguments] < team_output [ > team_input ]

from sys import stdin, argv
import os
import sys
import re

input_file = argv[1]
ans_file = argv[2]
feedback_dir = argv[3]

judge_feedback = open(os.path.join(feedback_dir, 'judgemessage.txt'), 'w')
team_feedback = open(os.path.join(feedback_dir, 'teammessage.txt'), 'w')


def check(res, msg='Wrong Answer', judge_msg=''):
    if not res:
        print >>team_feedback, msg
        print >>judge_feedback, judge_msg
        # Wrong Answer
        sys.exit(43)

integer = "(0|-?[1-9]\d*)"

line = stdin.readline()
check(re.match(integer + " " + integer + "\n", line), judge_msg='format error')

# Check for trailing input
check(len(stdin.readline()) == 0, judge_msg='format error')


# check ans
a, b = [int(x) for x in line.split(" ")]

x = int(open(input_file).readline())
check(0 <= a <= 1000, judge_msg='a = {} is out of range'.format(a))
check(0 <= b <= 1000, judge_msg='b = {} is out of range'.format(b))
check(a + b == x, judge_msg='a + b = {}, but should be {}'.format(a + b, x))

# Correct
sys.exit(42)
