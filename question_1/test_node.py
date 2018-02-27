from unittest import TestCase

from question_1.employee import Employee
from question_1.node import Node


class TestNode(TestCase):
    def setUp(self):
        self.emp_1 = Employee(1, "Employee", "One", "x", "department")
        self.emp_2 = Employee(2, "Employee", "Two", "x", "department")
        self.emp_3 = Employee(3, "Employee", "Three", "x", "department")

        self.node_1 = Node(self.emp_1)
        self.node_2 = Node(self.emp_2)
        self.node_3 = Node(self.emp_3)

    def test_add_child_no_children(self):
        """
        Test that the solution
        :return:
        """
        test = self.node_1.add_child(self.node_2)

        self.assertTrue(test)

        self.assertIsNotNone(self.node_1.child_nodes)
        self.assertEqual(self.node_1.child_nodes[0].data.id, self.emp_2.id)

    def test_add_child_has_children(self):
        test = self.node_1.add_child(self.node_2)

        self.assertTrue(test)
        self.node_1.add_child(self.node_3)

        self.assertEqual(self.node_1.child_nodes[len(self.node_1.child_nodes) - 1].data.id, self.emp_3.id)

    def test_add_child_node_is_none(self):
        test = self.node_1.add_child(None)

        self.assertFalse(test)

    def test_delete_child(self):
        self.node_1.add_child(self.node_2)
        self.node_1.delete_child(self.node_2)

        self.assertNotIn(self.node_2, self.node_1.child_nodes)

    def test_delete_child_node_is_none(self):
        self.node_1.add_child(None)
        test = self.node_1.delete_child(self.node_2)

        self.assertFalse(test)
        self.assertNotIn(None, self.node_1.child_nodes)
