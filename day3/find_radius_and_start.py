#!/usr/bin/env python
import sys

try:
	puzzle_input = int(sys.argv[1])
except:
	puzzle_input = 312051

def sval(r):
  p = (1 if r == 0 else sval(r - 1))
  return r * 8 + p

def find_radius(vin):
	r = 0
	vout = sval(r)
	while vout < vin:
		r += 1
		vout = sval(r)
	return (r, vout)

radius, start = find_radius(puzzle_input)
print "radius: %d  start: %d" % (radius, start)
