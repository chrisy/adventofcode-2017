#!/usr/bin/env python
import sys

try:
	input_file = sys.argv[1]
except:
	input_file = "input.txt"

with open(input_file) as fp:
	banks = [int(v.strip()) for v in fp.read().split("\t")]

cache = {}
cache[tuple(banks)] = True

count = 0
while True:
	print repr(banks)
	# find the most utilized bank
	mval = -1
	midx = -1
	for idx in range(len(banks)):
		if banks[idx] > mval:
			mval = banks[idx]
			midx = idx

	# redistribute its balance
	banks[midx] = 0
	while mval > 0:
		midx += 1
		if midx >= len(banks):
			midx = 0
		banks[midx] += 1
		mval -= 1

	count += 1

	# check history
	k = tuple(banks)
	if k in cache:
		break
	cache[k] = True


print "iterations: %d" % count
