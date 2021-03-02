class Node:
    def __init__(self, label: str, adjacent_nodes: ['Node'] = None) -> None:
        self.label = label
        self.adjacent_nodes = adjacent_nodes

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.label


# 两种pop的策略

def dfs_connected_iterative(graph: [Node]) -> [Node]:
    # 迭代 iterative
    # 时间：O(n^2)或者更准确说是Θ(e) ⊆ O(n^2)
    # 空间：Θ(n)
    if not graph:
        return []
    stack = [graph[0]]
    visited = set()
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            stack += filter(lambda n: n not in visited, node.adjacent_nodes)
    return order


def dfs_connected_recursive(graph):
    # 递归 recursive
    # 时间：O(n^2)或者更准确说是Θ(e) ⊆ O(n^2)
    # 空间：Θ(n)
    if not graph:
        return []
    visited = set()
    order = []

    def dfs_connected_recursive_node(node):
        if node not in visited:
            visited.add(node)
            order.append(node)
            for n in node.adjacent_nodes:
                if n not in visited:
                    dfs_connected_recursive_node(n)

    dfs_connected_recursive_node(graph[0])
    return order


def dfs_unconnected(graph):
    pass


def dfs_tree(tree):
    pass


def dfs_binary_tree(tree):
    pass


# empty graph
print(dfs_connected_iterative([]))
print(dfs_connected_recursive([]))

# a -- b -- c
# |    |    |
# d -- e -- f
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.adjacent_nodes = [b, d]
b.adjacent_nodes = [a, c, e]
c.adjacent_nodes = [b, f]
d.adjacent_nodes = [a, e]
e.adjacent_nodes = [b, d, f]
f.adjacent_nodes = [c, e]
print(dfs_connected_iterative([a, b, c, d, e, f]))
print(dfs_connected_recursive([a, b, c, d, e, f]))

#      a
#     / \
#    /   \
#   b     c
#  / \   / \
# d   e f   g
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.adjacent_nodes = [b, c]
b.adjacent_nodes = [a, d, e]
c.adjacent_nodes = [a, f, g]
d.adjacent_nodes = [b]
e.adjacent_nodes = [b]
f.adjacent_nodes = [c]
g.adjacent_nodes = [f]
print(dfs_connected_iterative([a, b, c, d, e, f, g]))
print(dfs_connected_recursive([a, b, c, d, e, f, g]))
