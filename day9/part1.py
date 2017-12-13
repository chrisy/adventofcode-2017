#!/usr/bin/env python
import sys

try:
	input_file = sys.argv[1]
except:
	input_file = "input.txt"

streams = []
with open(input_file) as fp:
	for line in fp:
		streams.append(line.strip())

for stream in streams:
	groups = 0
	score = 0
	tally = 0

	skip = False
	garbage = False

	for ch in list(stream):
		if skip:
			skip = False
			continue

		if ch == "!":
			skip = True
			continue

		if garbage:
			if ch == ">":
				garbage = False
		else:
			if ch == "{":
				groups += 1
				tally += 1
			elif ch == "}":
				score += tally
				tally -= 1
			elif ch == "<":
				garbage = True


	print "groups: %d score: %d" % (groups, score)
