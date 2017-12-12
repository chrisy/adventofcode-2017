#!/usr/bin/env python
import sys

try:
	input_file = sys.argv[1]
except:
	input_file = "input.txt"

program = []
with open(input_file) as fp:
	for line in fp:
		program.append([v.strip() for v in line.split(" ")])

registers = {}
peakvalue = 0

def read(register):
	global registers
	return registers.get(register, 0)

def inc(register, amount):
	global registers
	global peakvalue
	registers[register] = read(register) + amount
	if registers[register] > peakvalue:
		peakvalue = registers[register]

def dec(register, amount):
	global registers
	global peakvalue
	registers[register] = read(register) - amount
	if registers[register] > peakvalue:
		peakvalue = registers[register]


def regcmp(register, operator, value):
	if operator == "==":
		return read(register) == value
	if operator == "<":
		return read(register) < value
	if operator == ">":
		return read(register) > value
	if operator == "<=":
		return read(register) <= value
	if operator == ">=":
		return read(register) >= value
	if operator == "!=":
		return read(register) != value
	raise RuntimeError("unknown operator %s" % operator)


for line in program:
	sreg, opcode, sval, _if, creg, operator, cval = line
	sval = int(sval)
	cval = int(cval)
	assert _if == "if"

	if regcmp(creg, operator, cval):
		if opcode == "inc":
			inc(sreg, sval)
		elif opcode == "dec":
			dec(sreg, sval)

# find largest register value
rvals = sorted(registers.keys(), key=lambda k: registers[k])
print "reg %s val %d peak %d" % (rvals[-1], registers[rvals[-1]], peakvalue)
