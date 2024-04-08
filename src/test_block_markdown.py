import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks_empty(self):
        self.assertEqual(
            markdown_to_blocks(""),
            []
        )

    def test_markdown_to_blocks_3_blocks(self):
        self.assertEqual(
            markdown_to_blocks("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is a list item\n* This is another list item"),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is a list item\n* This is another list item"
             ]
        )

    def test_markdown_to_blocks_excessive_newlines(self):
        self.assertEqual(
            markdown_to_blocks("First line\n\n\n\nSecond line"),
            [
                "First line",
                "Second line"
            ]
        )


if __name__ == "__main__":
    unittest.main()