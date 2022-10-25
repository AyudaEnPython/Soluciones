"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Any, Optional, List
from dataclasses import dataclass
# pip install prototools
from prototools import build_tree


@dataclass
class Node:
    value: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __str__(self):
        lines = build_tree(self, 0, False, "-")[0]
        return "\n".join(line.rstrip() for line in lines)


def search(root: Node, value: Any) -> Optional[Node]:
    if root is None or root.value == value:
        return root
    if root.value < value:
        return search(root.right, value)
    return search(root.left, value)


def preorder(root: Node, output: List[Node]) -> List[Node]:
    if root.value is not None:
        output.append(root.value)
    if root.left is not None:
        preorder(root.left, output)
    if root.right is not None:
        preorder(root.right, output)
    return output


if __name__ == "__main__":
    root = Node(
        15,
        Node(
            10,
            Node(8),
            Node(12),
        ),
        Node(
            20,
            Node(16),
            Node(25),
        ),
    )
    print(root)
    print(search(root, 16))
    print(preorder(root, []))
