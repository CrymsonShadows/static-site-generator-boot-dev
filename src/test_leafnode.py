import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_children(self):
        p_node = LeafNode("p", "This is a paragraph of text.")
        a_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            p_node.to_html(),
            '<p>This is a paragraph of text.</p>'
        )
        self.assertEqual(
            a_node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_to_html_no_tag(self):
        node = LeafNode(value="Grapes!")
        self.assertEqual(
            node.to_html(),
            "Grapes!"
        )

if __name__ == "__main__":
    unittest.main()