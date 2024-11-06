from heaps import *

def test_get_tree_string():
    tree_1 = Tree(Node(7))
    tree_2 = Tree(Node(4, [Node(5)]))
    tree_3 = Tree(Node(1, [Node(2, [Node(3), Node(4)]), Node(5)]))
    assert tree_1.get_tree_string() == "7"
    assert tree_2.get_tree_string() == "4\n└──5"
    assert tree_3.get_tree_string() == "1\n├──2\n│  ├──3\n│  └──4\n└──5"
    print("Test test_get_tree_string succeeded!")


if __name__ == "__main__":
    test_get_tree_string()
