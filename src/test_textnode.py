import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_equal(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode('This is the first text node', TextType.BOLD)
        node2 = TextNode('This is the second text node', TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_text_types(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode('This is a text node', TextType.LINK, None)
        node2 = TextNode('This is a text node', TextType.LINK, 'www.emrysfitton.com')
        node3 = TextNode('This is a text node', TextType.LINK)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)
        self.assertEqual(node, node3)

if __name__ == '__main__':
    unittest.main()