#!/usr/bin/env python

def valid(line):
	cache = {}

	for word in line.split(" "):
		ws = tuple(sorted([w for w in word]))
		if ws in cache:
			return False
		cache[ws] = True

	return True

count = 0
with open("input.txt") as fp:
	for line in fp:
		if valid(line.strip()):
			count += 1

print "valid: %d" % count
