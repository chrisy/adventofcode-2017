#!/usr/bin/env python
import sys

try:
	input_file = sys.argv[1]
except:
	input_file = "input.txt"

# ugml (68) -> gyxo, ebii, jptl
items = {}

with open(input_file) as fp:
	for line in fp:
		line = line.strip()
		parts = line.split(" ")

		name = parts[0]
		weight = int(parts[1][1:-1])

		if len(parts) > 2:
			post = ("".join(parts[3:])).split(',')
		else:
			post = []

		items[name] = {
			'weight': weight,
			'post': post
		}


nodes = {}

class Node(object):
	weight = None
	children = None
	parents = None

	def __init__(self, weight):
		super(Node, self).__init__()
		self.weight = weight
		self.children = []
		self.parents = []

# first create all the nodes
for name in items.keys():
	nodes[name] = Node(items[name]['weight'])

# now link up the tree
for name in items.keys():
	node = nodes[name]
	for child in items[name]['post']:
		n = nodes[child]
		node.children.append(n)
		n.parents.append(node)

# find the root
# it's the one with no parents
for name in nodes.keys():
	node = nodes[name]
	if len(node.parents) == 0:
		print "no parents: %s" % name

