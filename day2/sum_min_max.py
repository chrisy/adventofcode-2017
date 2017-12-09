#!/usr/bin/python

# Extract the input
input_rows = []
with open("input.txt") as fp:
	for line in fp:
		input_rows.append([int(v.strip()) for v in line.split("\t")])


s = 0
for row in input_rows:
	s += max(row) - min(row)

print "sum: %d" % s
