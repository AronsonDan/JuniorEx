from question_1.node import Node


class HierarchicalTree:
    def __init__(self, root=None):
        self.root = root

    def add_employee(self, data, manager_id=None):
        """
        A function that adds a new employee to the organizational structure
        :param data: employee's data
        :param manager_id: the employee id of the manager
        :return: root of the tree
        """

        # if manager id is not supplied or is not found within the tree,
        # set the employee as the root of the tree(CEO)
        # else,
        # set the manager as the parent_node of the new node,

        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            manager = self.get_node(manager_id)

            if manager_id is None or manager is None:
                node.child_nodes = [self.root]
                self.root.parent_node = node
                self.root = node
            else:
                node.parent_node = manager
                manager.add_child(node)
        return self.root

    def delete_employee(self, employee_id):
        """
        A function which deletes an employee from the organizational structure
        :param employee_id: the UUID of the employee to delete
        :return:  the data of the requested employee to delete, in case
        """
        node_to_delete = self.get_node(employee_id)
        if node_to_delete is None:
            return None
        # if the employee id is the root of the node, set the root to None
        if node_to_delete == self.root:
            self.root = None
            return node_to_delete

        # remove the employee to delete from the children array of its parent
        parent_node = node_to_delete.parent_node
        parent_node.delete_child(node_to_delete)

        # in case the employee to delete has child nodes,
        # add the child nodes to its parent
        for child in node_to_delete.child_nodes:
            child.parent_node = parent_node
            parent_node.add_child(child)

        return node_to_delete.data

    def get_employee(self, employee_id):
        """
        A function which returns the requested employee by employee id
        :param employee_id:
        :return:
        """
        return self.get_node(employee_id)

    def get_first_shared_manager(self, employee_id_1, employee_id_2):
        """
        A function which returns the first manager who manages
        the two requested employees
        :param employee_id_1:
        :param employee_id_2:
        :return: the Node of the shared manager in case exists
        """
        # if one of the employee id's is invalid, return None
        if self.get_node(employee_id_1) is None or self.get_node(employee_id_2) is None:
            return None

        employee_1 = self.get_node(employee_id_1)
        # drill down and search whether employee id 2 is nested
        # within a sub-tree in which the root node is employee 1
        # in case not, set the new root as the parent node of employee 1
        while employee_1:
            if self.get_node(employee_id_2, employee_1):
                return employee_1
            else:
                employee_1 = employee_1.parent_node
        return None

    def get_node(self, employee_id, root=None):
        """
        A search method that runs through the nodes of the tree and finds an employee by the employee ID
        :param employee_id: the id of the employee that wants to be found
        :param root: the root of the sub-tree
        :return: a node of employee in case found
        """
        if self.root is None or employee_id is None:
            return None
        elif root is None:
            tree_arr = [self.root]
        else:
            tree_arr = [root]
        while len(tree_arr) > 0:
            node = tree_arr.pop(0)
            if node.data.id == employee_id:
                return node
            for child in node.child_nodes:
                tree_arr.append(child)

        return None
