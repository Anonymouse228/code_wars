# https://www.codewars.com/kata/52bef5e3588c56132c0003bc


class Node:
    def __init__(self, value, left=None, right=None):  # type: (int, Node|None, Node|None) -> None
        self.left = left
        self.right = right
        self.value = value


def tree_by_levels(node):  # type: (Node|None) -> list
    queue = [node] if node else []
    answer = []

    while queue:
        node = queue.pop(0)

        answer.append(node.value)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return answer


if __name__ == '__main__':
    n = Node(4)
    print(tree_by_levels(n))
