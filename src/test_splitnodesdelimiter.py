import unittest

from textnode import split_nodes_delimiter, TextNode, text_type_text, text_type_bold

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_empty_nodes(self):
        self.assertEqual(
            split_nodes_delimiter([], "`", text_type_text),
            []
        )

    def test_one_old_node_one_bold_node_inside(self):
        node = TextNode("This is just a text node of type text with **bold** inside.", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "**", text_type_bold),
            [
                TextNode("This is just a text node of type text with ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" inside.", text_type_text)
            ]
        )

    def test_one_old_node_just_bold_text(self):
        node = TextNode("**HI**", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "**", text_type_bold),
            [
                TextNode("HI", text_type_bold),
            ]
        )

if __name__ == "__main__":
    unittest.main()