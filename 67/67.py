#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#3
#7 4
#2 4 6
#8 5 9 3

#That is, 3 + 7 + 4 + 9 = 23.

#Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

#NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)


class Tree():

    def __init__(self, tiers=[]):
        self.tiers = tiers
        self.tree_length = len(self.tiers)
        self.node_map = self._init_node_map()
        nodes = self.nodify()
        self.link_nodes()
        self.max_sum = self.node_map[0][0].max_sum

    def _init_node_map(self):
        node_map = {}
        for depth in range(0, self.tree_length):
            node_map[depth] = []
        return node_map

    def nodify(self):
        nodes = []
        for depth in range(0, self.tree_length):
            for index in range(0, len(self.tiers[depth])):
                current_node = Node(self.tiers[depth][index], depth, index)
                nodes.append(current_node)
                self.node_map[depth].append(current_node)
        return nodes

    def link_nodes(self):
        for depth in range(self.tree_length-1, -1, -1):
            for node in self.node_map[depth]:
                if depth == (self.tree_length - 1):
                    node.max_sum = node.value
                else:
                    for x in self.node_map[depth+1]:
                        if x.index == node.index:
                            node.left = x
                            x.parents.append(node)
                        if x.index == node.index + 1:
                            node.right = x
                            x.parents.append(node) 
                    node.max_sum = node.value + max(
                            node.left.max_sum, node.right.max_sum)

class Node():

    def __init__(self, value=None, depth=0, index=0):
        self.value = value
        self.depth = depth
        self.index = index
        self.parents = []
        self.left = None
        self.right = None
        self.max_sum = None


def get_tree(tree_file):
    f = open(tree_file)
    tree = []
    for line in f:
        new_tier = []
        tier = line.split(' ')
        for i in tier:
            new_tier.append(int(i))
        tree.append(new_tier)
    return tree


tree = Tree(get_tree('triangle.txt'))

print tree.max_sum
