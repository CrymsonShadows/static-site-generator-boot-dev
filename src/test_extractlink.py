from extractlink import extract_markdown_images, exttract_markdown_links
import unittest

class TestExtractLink(unittest.TestCase):
    def test_extract_markdown_images_one_image(self):
        text = "![image](https://i.imgur.com/zjjcJKZ.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [("image", "https://i.imgur.com/zjjcJKZ.png")]
        )

    def test_extract_markdown_images_two_images_in_text(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        )

    def test_extract_markdown_link(self):
        text = "[link](https://www.example.com)"    
        self.assertEqual(
            exttract_markdown_links(text),
            [("link", "https://www.example.com")]
        )

    def test_extract_markdown_links_in_text(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(
            exttract_markdown_links(text),
            [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        )


if __name__ == "__main__":
    unittest.main()