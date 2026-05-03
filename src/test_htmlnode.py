import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_equal_empty(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_different(self):
        node = HTMLNode()
        node2 = HTMLNode('h1', 'test case')
        self.assertNotEqual(node, node2)

    def test_props(self):
        node = HTMLNode('h1', 'test case')
        output = f'HTMLNode(h1, test case, None, None)'
        self.assertEqual(repr(node), output)