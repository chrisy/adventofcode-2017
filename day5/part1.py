#!/usr/bin/env python
import sys

try:
	input_file = sys.argv[1]
except:
	input_file = "input.txt"

with open(input_file) as fp:
	program = [int(v.strip()) for v in fp]

ip = 0
steps = 0
while ip < len(program):
	old_ip = ip
	ip += program[ip]
	program[old_ip] += 1
	steps += 1

print "steps: %d" % steps
