import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, block_type_paragraph, block_type_heading, block_type_code, block_type_quote, block_type_unordered_list, block_type_ordered_list

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

    def test_block_to_block_type_paragraph_block(self):
        self.assertEqual(
            block_to_block_type("This is a paragraph.\nThis is the second line of the paragraph."),
            block_type_paragraph
        )

    def test_block_to_block_type_heading_1(self):
        self.assertEqual(
            block_to_block_type("# This is a heading"),
            block_type_heading
        )

    def test_block_to_block_type_heading_2(self):
        self.assertEqual(
            block_to_block_type("## This is a subheading"),
            block_type_heading
        )

    def test_block_to_block_type_code(self):
        self.assertEqual(
            block_to_block_type("```This is code```"),
            block_type_code
        )

    def test_block_to_block_type_code_no_trailing_backticks(self):
        self.assertEqual(
            block_to_block_type("```This code block doesn't end with backticks"),
            block_type_paragraph
        )

    def test_block_to_block_type_code_no_starting_backticks(self):
        self.assertEqual(
            block_to_block_type("This code block has no starting backticks```"),
            block_type_paragraph
        )

    def test_block_to_block_type_quote(self):
        self.assertEqual(
            block_to_block_type("> This the first line of a quote\n> This is the second line of a quote"),
            block_type_quote
        )
    
    def test_block_to_block_type_quote_only_one_line_with_arrow(self):
        self.assertEqual(
            block_to_block_type("> This is the first line of the quote\nThis is the second line without the arrow"),
            block_type_paragraph
        )

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(
            block_to_block_type("* This is the first item on the list\n- This is the second item"),
            block_type_unordered_list
        )

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(
            block_to_block_type("* First item\nSecond line"),
            block_type_paragraph
        )

    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(
            block_to_block_type("1. First item\n2. Second Item\n3. Third item"),
            block_type_ordered_list
        )

    def test_block_to_block_type_odered_list_out_of_order_lines(self):
        self.assertEqual(
            block_to_block_type("1. First item\n3.Second item"),
            block_type_paragraph
        )

if __name__ == "__main__":
    unittest.main()