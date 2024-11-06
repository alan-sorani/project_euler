from __future__ import annotations
import numpy as np
import sympy
from typing import Callable, TypeVar
from functools import cache

    tree_1 = Tree(Node(7))
    tree_2 = Tree(Node(4, [Node(5)]))
    tree_3 = Tree(Node(1, [Node(2, [Node(3), Node(4)]), Node(5)]))
    assert tree_1.get_tree_string() == "7"
    assert tree_2.get_tree_string() == "4\n└──5"
    assert tree_3.get_tree_string() == "1\n├──2\n│  ├──3\n│  └──4\n└──5"

class Node:
    def __init__(
            self,
            value,
            children : list[Node] | None = None,
            parents : list[Node] | None = None
        ):
        self.value = value
        self.children = children if children else []
        self.parents = parents if parents else []

class Tree:
    def __init__(
            self,
            root : Node | None = None
        ):
        self.root = root
        self.depth = self.get_depth()

    def get_depth(self):
        if(self.root == None):
            return 0
        if(self.root.children == []):
            return 1
        return 1 + max([
            Tree(child).get_depth() for child in self.root.children
        ])

    def get_tree_string(self):
        if(self.depth == 0):
            return "[Empty Tree]"
        if(self.depth == 1):
            return str(self.root.value)
        res = str(self.root.value) + "\n"
        children = self.root.children
        rank = len(children)
        for i in range(rank):
            subtree = Tree(children[i])
            subtree_string_lines = subtree.get_tree_string().split('\n')
            num_lines = len(subtree_string_lines)
            for j in range(num_lines):
                if(j == 0):
                    if(i < rank - 1):
                        res += "├──" 
                    else:
                        res += "└──"
                else:
                    res += "│  "
                res += subtree_string_lines[j]
                res += "\n"
        return res[:-1]

class Heap:
    def __init__(self)

if __name__ == "__main__":
