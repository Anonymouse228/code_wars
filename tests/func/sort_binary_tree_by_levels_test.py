import pytest

from sort_binary_tree_by_levels import Node, tree_by_levels

data = [
    (None, []),
    (Node(1, Node(2, None, Node(4)), Node(3, Node(5), Node(6))), [1, 2, 3, 4, 5, 6]),
    (Node(1, Node(8, None, Node(3)), Node(4, None, Node(5, None, Node(7)))), [1, 8, 4, 3, 5, 7]),
    (Node(2, Node(8, Node(1), Node(3)), Node(9, Node(4), Node(5))), [2, 8, 9, 1, 3, 4, 5]),
]


@pytest.mark.parametrize('node, answer', data)
def test_answers(node, answer):
    assert tree_by_levels(node) == answer
