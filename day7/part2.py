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

	def __init__(self, name, weight):
		super(Node, self).__init__()
		self.name = name
		self.weight = weight
		self.children = []
		self.parents = []

	def sum_weights(self):
		weight = self.weight
		weight += sum([n.sum_weights() for n in self.children])
		return weight

	def dump_weights(self, path=None):
		if not path:
			path = ""
		path = "%s %s" % (path, self.name)

		weight = self.sum_weights()
		print "%s = %d" % (path, weight)

		weights = [n.sum_weights() for n in self.children]
		#print repr(weights)

		for child in self.children:
			child.dump_weights(path)

	def find_imbalance(self, path=None):
		if not path:
			path = self.name
		else:
			path = "%s %s" % (path, self.name)

		# apparently one may be wrong, work out which one it is
		cache = {}
		for child in self.children:
			w = child.sum_weights()
			if w not in cache:
				cache[w] = [child]
			else:
				cache[w].append(child)

		if len(cache.keys()) > 1:
			keys = sorted(cache.keys(), key=lambda k: len(cache[k]))
			_p = ["%d:%d" % (k, len(cache[k])) for k in keys]
			print "%d [%s] unbalanced %s diff %d val %d cval %d" % (self.weight, path, ", ".join(_p), keys[0] - keys[1], cache[keys[0]][0].weight, cache[keys[0]][0].weight - (keys[0] - keys[1]))
			cache[keys[0]][0].find_imbalance(path)

	def compare_weights(self):
		weights = [n.sum_weights() for n in self.children]
		print repr(weights)

		[n.compare_weights() for n in self.children]

# first create all the nodes
for name in items.keys():
	nodes[name] = Node(name, items[name]['weight'])

# now link up the tree
for name in items.keys():
	node = nodes[name]
	for child in items[name]['post']:
		n = nodes[child]
		node.children.append(n)
		n.parents.append(node)

# find the root
# it's the one with no parents
root = None
for name in nodes.keys():
	node = nodes[name]
	if len(node.parents) == 0:
		root = node
		break

if root is None:
	raise RuntimeError("No root")

root.find_imbalance()
#root.compare_weights()

