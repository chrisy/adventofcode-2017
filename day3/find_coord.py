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
	prev = vout = sval(r)
	while vout <= vin:
		r += 1
		prev = vout
		vout = sval(r)
	return (r, prev)

radius, start = find_radius(puzzle_input)
print "radius: %d  start: %d" % (radius, start)
width = (radius * 2) + 1
square_length = (width - 1) * 4
linear_position = puzzle_input - start
#if linear_position == 0:
#	linear_position += square_length
segment = linear_position // 4
segment_position = linear_position % (width - 1)
print "width: %d  length: %d linear_position: %d  segment: %d  segment_position: %d" % (
	width, square_length, linear_position, segment, segment_position)

# the exact coord with origin at the center is not necessary,
# we know one is the radius and the other is abs((width/2) - segment_position)

a = radius
b = (width // 2) - segment_position

# account for the start of a string not being where our model says it
# is
if linear_position == 0:
	a -= 1
	b -= 1

print "a: %d  b: %d  total: %d" % (a, b, a + abs(b))

