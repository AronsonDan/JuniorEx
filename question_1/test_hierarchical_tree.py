from unittest import TestCase
from question_1.node import Node
from question_1.employee import Employee
from question_1.hierarchical_tree import HierarchicalTree


class TestHierarchicalTree(TestCase):
    def setUp(self):

        self.employee_to_add = Employee(6, "Employee", "Six", "x", "department")

        emp_1 = Employee(1, "Employee", "One", "x", "department")
        emp_2 = Employee(2, "Employee", "Two", "x", "department")
        emp_3 = Employee(3, "Employee", "Three", "x", "department")
        emp_4 = Employee(4, "Employee", "Four", "x", "department")
        emp_5 = Employee(5, "Employee", "Five", "x", "department")
        emp_7 = Employee(7, "Employee", "Seven", "x", "department")
        emp_8 = Employee(8, "Employee", "Eight", "x", "department")

        self.node_1 = Node(emp_1)
        self.node_2 = Node(emp_2)
        self.node_3 = Node(emp_3)
        self.node_4 = Node(emp_4)
        self.node_5 = Node(emp_5)
        self.node_7 = Node(emp_7)
        self.node_8 = Node(emp_8)

        self.node_2.parent_node = self.node_1
        self.node_1.child_nodes = [self.node_2, self.node_3]
        self.node_3.parent_node = self.node_1
        self.node_3.child_nodes = [self.node_4, self.node_5]
        self.node_4.parent_node = self.node_3
        self.node_5.parent_node = self.node_3
        self.node_4.child_nodes = [self.node_7, self.node_8]
        self.node_7.parent_node = self.node_4
        self.node_8.parent_node = self.node_4

        self.hierarchical_tree = HierarchicalTree(self.node_1)

    def tearDown(self):
        self.hierarchical_tree = None

    def test_get_node_with_return(self):
        node = self.hierarchical_tree.get_node(1)
        self.assertEqual(node, self.node_1)

    def test_get_node_with_none_return(self):
        node = self.hierarchical_tree.get_node(99)
        self.assertIsNone(node)

    def test_add_employee(self):
        self.hierarchical_tree.add_employee(self.employee_to_add, self.node_4.data.id)

        self.assertEqual(self.hierarchical_tree.get_node(6).parent_node, self.node_4)
        self.assertIn(self.hierarchical_tree.get_node(6), self.node_4.child_nodes)

    def test_add_employee_ceo(self):
        self.hierarchical_tree.add_employee(self.employee_to_add)

        self.assertEqual(self.hierarchical_tree.get_node(6).parent_node, None)
        self.assertEqual(self.hierarchical_tree.get_node(1).parent_node, self.hierarchical_tree.get_node(6))
        self.assertEqual(self.hierarchical_tree.get_node(6).child_nodes, [self.node_1])
        self.assertEqual(self.hierarchical_tree.root, self.hierarchical_tree.get_node(6))

    def test_add_employee_when_root_is_none(self):
        self.hierarchical_tree.root = None
        self.hierarchical_tree.add_employee(self.employee_to_add)

        self.assertEqual(self.hierarchical_tree.root.data.id, 6)

    def test_delete_employee_with_children(self):
        parent_id = self.hierarchical_tree.get_employee(3).parent_node.data.id

        self.hierarchical_tree.delete_employee(3)
        self.assertIsNone(self.hierarchical_tree.get_employee(3))

        parent_node = self.hierarchical_tree.get_employee(parent_id)
        self.assertNotIn(self.node_3, parent_node.child_nodes)
        self.assertIn(self.node_4, parent_node.child_nodes)
        self.assertIn(self.node_5, parent_node.child_nodes)
        self.assertEqual(self.hierarchical_tree.get_employee(4).parent_node, self.node_1)
        self.assertEqual(self.hierarchical_tree.get_employee(5).parent_node, self.node_1)

    def test_delete_employee_no_children(self):
        parent_id = self.hierarchical_tree.get_employee(5).parent_node.data.id
        self.hierarchical_tree.delete_employee(5)

        self.assertIsNone(self.hierarchical_tree.get_employee(5))

        parent_node = self.hierarchical_tree.get_employee(parent_id)
        self.assertNotIn(self.node_5, parent_node.child_nodes)

    def test_delete_employee_that_does_not_exist(self):
        self.assertIsNone(self.hierarchical_tree.delete_employee(256))

    def test_get_employee_that_exist(self):
        node = self.hierarchical_tree.get_employee(1)

        self.assertEqual(node.data.id, 1)
        self.assertEqual(node.parent_node, None)
        self.assertEqual(node.child_nodes, [self.node_2, self.node_3])

    def test_get_employee_that_does_not_exist(self):
        self.assertIsNone(self.hierarchical_tree.get_employee(100))

    def test_get_first_shared_manager_employee_id_valid(self):
        manager_node = self.hierarchical_tree.get_first_shared_manager(4, 2)
        self.assertEqual(manager_node, self.node_1)

        manager_node = self.hierarchical_tree.get_first_shared_manager(8, 5)
        self.assertEqual(manager_node, self.node_3)

        manager_node = self.hierarchical_tree.get_first_shared_manager(1, 7)
        self.assertEqual(manager_node, self.node_1)

    def test_get_first_shared_manager_employee_id_not_valid(self):
        self.assertIsNone(self.hierarchical_tree.get_first_shared_manager(100, 2))
        self.assertIsNone(self.hierarchical_tree.get_first_shared_manager(1, 8787))
