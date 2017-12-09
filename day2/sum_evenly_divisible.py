#!/usr/bin/python

# Extract the input
input_rows = []
with open("input.txt") as fp:
	for line in fp:
		input_rows.append([int(v.strip()) for v in line.split("\t")])


s = 0
for row in input_rows:
	for t in row:
		for b in [v for v in row if v < t]:
			if (t % b) == 0:
				s += t / b
				break

print "sum: %d" % s
