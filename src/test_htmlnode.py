import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props_a(self):
        node = HTMLNode("a", "google", None, {"href": "https://www.google.com"})
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com"'
        )

    def test_to_html_props_a_gt_2_props(self):
        node = HTMLNode("a", "google", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

if __name__ == "__main__":
    unittest.main()