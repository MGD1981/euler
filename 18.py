# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

        # 3
       # 7 4
      # 2 4 6
     # 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

                            # 75
                           # 95 64
                          # 17 47 82
                         # 18 35 87 10
                        # 20 04 82 47 65
                       # 19 01 23 75 03 34
                      # 88 02 77 73 07 63 67
                     # 99 65 04 28 06 16 70 92
                    # 41 41 26 56 83 40 80 70 33
                   # 41 48 72 33 47 32 37 16 94 29
                  # 53 71 44 65 25 43 91 52 97 51 14
                 # 70 11 33 28 77 73 17 78 39 68 17 57
                # 91 71 52 38 17 14 91 43 58 50 27 29 48
               # 63 66 04 68 89 53 67 30 73 16 69 87 40 31
              # 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)



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


tree = Tree([[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]])

print tree.max_sum
