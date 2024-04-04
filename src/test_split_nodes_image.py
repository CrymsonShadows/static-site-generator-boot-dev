import unittest
from textnode import TextNode, text_type_text, text_type_image, split_nodes_image

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image_empty_node(self):
        node = TextNode("", text_type_text)
        self.assertEqual(
            split_nodes_image([node]),
            []
        )

    def test_split_nodes_image_only_one_image(self):
        node = TextNode("![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)", text_type_text)
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
            ]
        )

    def test_split_nodes_image_one_image_with_text_after(self):
        node = TextNode("![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and more text", text_type_text)
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and more text", text_type_text)
            ]
        )

    def test_split_nodes_image_two_images_in_text(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                ),
            ]
        )

    def test_split_nodes_image_two_images_no_in_between(self):
        node = TextNode(
            "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                 TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                 TextNode(
                    "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                )
            ]
        )

    def test_split_nodes_image_two_images_in_two_nodes(self):
        node_1 = TextNode("![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)", text_type_text)
        node_2 = TextNode(
            "![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text
        )
        self.assertEqual(
            split_nodes_image([node_1, node_2]),
            [
                 TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                 TextNode(
                    "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                )
            ]
        )

if __name__ == "__main__":
    unittest.main()