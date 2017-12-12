#!/usr/bin/env python

# ok, this problem may have a pattern but i frankly can't be arsed to
# search for it. instead just use an (x, y) tuple as a hash key, origin
# on the start value. suspect this is what they intended, for part 1,
# even though it's nasty.

storage = {
	(0, 0): 1,
}

def empty(xy):
	global storage
	return xy not in storage

def valueof(xy):
	return storage.get(xy, 0)

def nextxy(xy):
	x, y = xy

	# square right empty and square up filled, go right
	if empty((x+1, y)) and not empty ((x, y-1)):
		return (x+1, y)

	# square up empty and square left not empty, go up
	if empty((x, y-1)) and not empty((x-1, y)):
		return (x, y-1)

	# square left empty and square down not empty, go left
	if empty((x-1, y)) and not empty((x, y+1)):
		return (x-1, y)

	# square down empty, square right not empty, go down
	if empty((x, y+1)) and not empty((x+1, y)):
		return (x, y+1)

	# go right - bootstrap state
	return (x+1, y)

def print_storage():
	# get the extents of each dimension
	max_x = max([v[0] for v in storage.keys()])
	min_x = min([v[0] for v in storage.keys()])
	max_y = max([v[1] for v in storage.keys()])
	min_y = min([v[1] for v in storage.keys()])

    # print them
	for y in range(min_y, max_y+1):
		row = []
		for x in range(min_x, max_x+1):
			if empty((x, y)):
				row.append("     ")
			else:
				row.append("%5d" % storage[(x, y)])
		print " ".join(row)


def sum_adjacent(xy):
	x, y = xy
	v = 0

	v += valueof((x-1, y-1))
	v += valueof((x, y-1))
	v += valueof((x+1, y-1))

	v += valueof((x-1, y))
	v += valueof((x, y))
	v += valueof((x+1, y))

	v += valueof((x-1, y+1))
	v += valueof((x, y+1))
	v += valueof((x+1, y+1))

	return v


xy = (0, 0)
sa = 0
while sa <= 312051:
	sa = sum_adjacent(xy)
	storage[xy] = sa
	xy = nextxy(xy)

print "sa: %d" % sa
#print_storage()
