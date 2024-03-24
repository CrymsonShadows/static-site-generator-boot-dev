import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def one_layer_children(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(
            node.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

    def one_layer_children_parent_one_prop(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        {
            "id": "normal"
        }
        )
        self.assertEqual(
            node.to_html(),
            '<p id="normal"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

    def two_layers_children(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "normal text")
                    ]
                )
            ]
        )
        self.assertEqual(
            node.to_html(),
            '<div><p>normal text</p></div>'
        )
if __name__ == "__main__":
    unittest.main()