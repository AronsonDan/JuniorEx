class Node:
    def __init__(self, data, parent_node=None, child_nodes=[]):
        self.data = data
        self.parent_node = parent_node
        self.child_nodes = child_nodes

    def add_child(self, node):
        """
        A function to add a child node to the child_nodes attribute
        :param node:
        :return: True in case of success False in case not
        """
        if node is not None:
            self.child_nodes.append(node)
            if node in self.child_nodes:
                return True
        return False

    def delete_child(self, node):
        """
        A function that deletes a child from the child_nodes array
        :param node: a node that is to be deleted from the array
        :return: True in case of success False in case not
        """
        if node in self.child_nodes:
            self.child_nodes.remove(node)
            return True
        return False
