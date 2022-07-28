import re

from node import Node


def split_at_inc(index: int, data: list[int]):
    if len(data) == index:
        return [data]

    first = data[:index]
    last = data[index:]

    return split_at_inc(index + 1, last) + [first]


def create_tree(data: list[list[int]], children: list[Node]):
    if len(children) == 1:
        return children[0]

    neighbors = list(map(lambda x: Node(x), data[0]))

    if len(children) != 0:
        for i, neighbor in enumerate(neighbors):
            neighbor.left = children[i]
            neighbor.right = children[i + 1]

    return create_tree(data[1:], neighbors)


def max_path(n: Node):
    if n.left is None or n.right is None:
        n.max_path = n.val

    if n.max_path is None:
        n.max_path = n.val + max(max_path(n.left), max_path(n.right))

    return n.max_path


def read_triangle(filename: str):
    with open(filename) as f:
        t = re.split(r"\s", f.read())
        return list(map(lambda x: int(x), t))


if __name__ == '__main__':
    tree = create_tree(split_at_inc(1, read_triangle("p067_triangle.txt")), [])
    print(max_path(tree))
