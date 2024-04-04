import unittest
from textnode import TextNode, text_type_text, text_type_link, split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link_empty_node(self):
        node = TextNode("", text_type_text)
        self.assertEqual(
            split_nodes_link([node]),
            []
        )

    def test_split_nodes_link_only_one_link(self):
        node = TextNode("[link](https://www.example.com)", text_type_text)
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("link", text_type_link, "https://www.example.com")
            ]
        )

    def test_split_nodes_link_two_links_in_text(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            text_type_text,
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
                TextNode(" and ", text_type_text),
                TextNode(
                    "another", text_type_link, "https://www.example.com/another"
                ),
            ]
        )

    def test_split_nodes_link_two_links_no_in_between(self):
        node = TextNode(
            "[link](https://www.example.com)[another](https://www.example.com/another)",
            text_type_text
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                 TextNode("link", text_type_link, "https://www.example.com"),
                 TextNode(
                    "another", text_type_link, "https://www.example.com/another"
                )
            ]
        )

    def test_split_nodes_link_two_links_in_two_nodes(self):
        node_1 = TextNode("[link](https://www.example.com)", text_type_text)
        node_2 = TextNode(
            "[another](https://www.example.com/another)",
            text_type_text
        )
        self.assertEqual(
            split_nodes_link([node_1, node_2]),
            [
                 TextNode("link", text_type_link, "https://www.example.com"),
                 TextNode(
                    "another", text_type_link, "https://www.example.com/another"
                )
            ]
        )

if __name__ == "__main__":
    unittest.main()