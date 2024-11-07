from __future__ import annotations
import numpy as np
import sympy
from typing import Callable, TypeVar
from functools import cache

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
        self.in_rank = len(self.parents)
        self.out_rank = len(self.children)

class MinHeap:
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
            MinHeap(child).get_depth() for child in self.root.children
        ])

    def link_tree(self, other : MinHeap):
        if(self.root.value < other.root.value):
            self.root.children += [other.root]
            other.root.parents += [self.root]
            self.depth = max([self.depth, other.depth + 1])
        else:
            other.root.children += [self.root]
            self.root.parents += [other.root]
            other.depth = max([other.depth, self.depth + 1])
            self.root = other.root
            self.depth = other.depth

    def get_string(self):
        if(self.depth == 0):
            return "[Empty Tree]"
        if(self.depth == 1):
            return str(self.root.value)
        res = str(self.root.value) + "\n"
        children = self.root.children
        rank = len(children)
        for i in range(rank):
            subtree = MinHeap(children[i])
            subtree_string_lines = subtree.get_string().split('\n')
            num_lines = len(subtree_string_lines)
            for j in range(num_lines):
                if(j == 0):
                    if(i < rank - 1):
                        res += "├──" 
                    else:
                        res += "└──"
                else:
                    res += "│  " if (i < rank - 1) else "   "
                res += subtree_string_lines[j]
                res += "\n"
        return res[:-1]

class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.min_node = None
    def add_tree(self, tree : MinHeap):
        self.trees += [tree]
        if((
            self.min_node == None
            ) or (
            tree.root.value < self.min_node.value
            )
        ):
            self.min_node = tree.root

    def get_string(self):
        res = ""
        for tree in self.trees:
            res += tree.get_string() + "\n\n"
        return res[:-2]

if __name__ == "__main__":
    tree_1 = MinHeap(Node(1, [Node(2), Node(3, [Node(4)])]))
    tree_2 = MinHeap(Node(5, [Node(6, [Node(7)]), Node(8, [Node(9)])]))
    heap = FibonacciHeap()
    heap.add_tree(tree_1)
    heap.add_tree(tree_2)
    print(heap.get_string())
