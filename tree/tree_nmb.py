

class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class Tree(object):

    def __init__(self, root):
        """
        Constructor to initiate the Tree object
        Generate the array of each layer of the tree
        :param root: (Node) the root node of the tree
        """
        self.root = root

    def get_value_root(self):
        """
        Get the value of the root node.
        :return: (int/str... or None) self.root.value or None
        """
        if self.root is not None:
            return self.root.value
        else:
            return None

    @classmethod
    def height(cls, node):
        """
        Recursive function to find path
        :param node: object
        :return: height: int
        """
        if node is None:
            h = 0

        else:
            left_height = cls.height(node.left)
            right_height = cls.height(node.right)

            if left_height < right_height:
                h = 1 + right_height

            else:
                h = 1 + left_height

        return h

    def print_tree(self):
        """
        Print the tree, first define a fill_tree function,
        then call the function fill_subtree to replace the blanks with correct node value
        :return: (list) a list that contains lists of rows in the tree
        """
        height = Tree.height(self.root)
        width = 2 ** height - 1

        tree_list = []
        tree_list.extend([["|"] * width for i in range(height)])

        def subtree(root, depth, left_end, right_end):
            """
            Fill the root node of a child tree, we know the each resulted list is with length 2n-1 .
            From the first layer, we fill the center
            Then we split the second layer to left and right halves,
            replace the center of the resulted left array with left node
            and do the same on the right node
            :param root: Node object
            :param depth: (int) from above, the number of row that the nodes to be filled by root
            :param left_end: (int) the extreme left end of the sub-tree
            :param right_end: (int) the extreme right end of the sub-tree
            :return: (none)
            """

            if root is None:
                return None

            else:
                center = int((left_end + right_end) / 2)
                tree_list[depth][center] = str(root.value)
                subtree(root.left, depth + 1, left_end, center - 1)
                subtree(root.right, depth + 1, center + 1, right_end)

        subtree(self.root, 0, 0, width-1)

        return tree_list

