import unittest
from textnode import TextNode, text_to_textnodes, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image, text_type_text

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnode_empty(self):
        self.assertEqual(
            text_to_textnodes(""),
            []
        )

    def test_text_to_textnode_only_bold(self):
        self.assertEqual(
            text_to_textnodes("**Boop**"),
            [
                TextNode("Boop", text_type_bold)
            ]
        )

    def test_text_to_textnode_only_italic(self):
        self.assertEqual(
            text_to_textnodes("*Boop*"),
            [
                TextNode("Boop", text_type_italic)
            ]
        )

    def test_text_to_textnode_only_code(self):
        self.assertEqual(
            text_to_textnodes("`Boop`"),
            [
                TextNode("Boop", text_type_code)
            ]
        )

    def test_text_to_textnode_only_image(self):
        self.assertEqual(
            text_to_textnodes("![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"),
            [
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
            ]
        )

    def test_text_to_textnode_only_link(self):
        self.assertEqual(
            text_to_textnodes("[link](https://boot.dev)"),
            [
                TextNode("link", text_type_link, "https://boot.dev")
            ]
        )

    def test_text_to_textnode_all_in_text(self):
        self.assertEqual(
            text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"),
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev")
            ]
        )