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
matched = 0
while matched < 2:
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
		print "iterations: %d" % count
		count = 0
		matched += 1
		cache = {}
	cache[k] = True
