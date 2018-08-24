import unittest

from tree.tree_nmb import Tree, Node


class TestTree(unittest.TestCase):

    def test1(self):
        """
        Test a single node tree
        :return:
        """
        a = Node(1, None, None)
        tree1 = Tree(a)
        assert tree1.print_tree() == [['1']]

    def test2(self):
        """
        Test a complete binary tree
        :return:
        """
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)
        e = Node(5, None, None)
        f = Node(6, None, None)
        g = Node(7, None, None)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.left = f
        c.right = g
        tree2 = Tree(a)

        assert tree2.print_tree() == [['|', '|', '|', '1', '|', '|', '|'],
                                      ['|', '2', '|', '|', '|', '3', '|'],
                                      ['4', '|', '5', '|', '6', '|', '7']]

    def test3(self):
        """
        Test a tree with only left child nodes
        :return:
        """
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)
        a.left = b
        b.left = c
        c.left = d
        tree3 = Tree(a)

        assert tree3.print_tree() == [['|'] * 7 + ['1'] + ['|'] * 7,
                                      ['|'] * 3 + ['2'] + ['|'] * 11,
                                      ['|'] + ['3'] + ['|'] * 13,
                                      ['4'] + ['|'] * 14]

    def test4(self):
        """
        Test a irregular shape tree
        :return:
        """
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)
        e = Node(5, None, None)
        f = Node(6, None, None)
        a.left = b
        a.right = c
        b.right = d
        c.left = e
        e.right = f
        tree4 = Tree(a)

        assert tree4.print_tree() == [['|'] * 7 + ['1'] + ['|'] * 7,
                                      ['|'] * 3 + ['2'] + ['|'] * 7 + ['3'] + ['|'] * 3,
                                      ['|'] * 5 + ['4'] + ['|'] * 3 + ['5'] + ['|'] * 5,
                                      ['|'] * 10 + ['6'] + ['|'] * 4]


