import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, block_type_paragraph, block_type_heading, block_type_code, block_type_quote, block_type_unordered_list, block_type_ordered_list, paragraph_block_to_html_node, quote_block_to_html_node, unordered_list_block_to_html_node, ordered_list_block_to_html_node
from htmlnode import ParentNode, LeafNode

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

    def test_block_to_block_type_ordered_list_out_of_order_lines(self):
        self.assertEqual(
            block_to_block_type("1. First item\n3.Second item"),
            block_type_paragraph
        )

    def test_blockquote_to_html_node(self):
        expected_HTML_node: ParentNode = ParentNode(tag="blockquote", children=[LeafNode(tag=None, value="This is within a blockquote")], props=None)
        self.assertEqual(
            quote_block_to_html_node("> This is within a blockquote").to_html(),
            expected_HTML_node.to_html()
        )

    def test_blockquote_to_html_node_two_lines(self):
        expected_HTML_node: ParentNode = ParentNode(tag="blockquote", children=[LeafNode(tag=None, value="First line<br>Second line")], props=None)
        self.assertEqual(
            quote_block_to_html_node("> First line\n> Second line").to_html(),
            expected_HTML_node.to_html()
        )

    def test_blockquote_to_html_node_bold_inline_elements(self):
        expected_HTML_node: ParentNode = ParentNode(tag="blockquote", children=[LeafNode(tag=None, value="First "), LeafNode(tag="b", value="BOLD"), LeafNode(tag=None, value="<br>Second line")], props=None)
        self.assertEqual(
            quote_block_to_html_node("> First **BOLD**\n> Second line").to_html(),
            expected_HTML_node.to_html()
        )

    def test_unordered_list_to_html_node(self):
        expected_html_node: ParentNode = ParentNode(
            tag="ul",
            children=[
                ParentNode(tag="li", children=[LeafNode(tag=None, value="First")], props=None),
                ParentNode(tag="li", children=[LeafNode(tag=None, value="Second")], props=None)
            ],
            props=None
        )
        self.assertEqual(
            unordered_list_block_to_html_node("* First\n- Second").to_html(),
            expected_html_node.to_html()
        )
        
    def test_unordered_list_to_html_node_bold_inline_element(self):
        expected_html_node: ParentNode = ParentNode(
            tag="ul",
            children=[
                ParentNode(tag="li", children=[LeafNode(tag="b", value="BOLD")], props=None),
                ParentNode(tag="li", children=[LeafNode(None, "Second")], props=None)
            ],
            props=None
        )
        self.assertEqual(
            unordered_list_block_to_html_node("* **BOLD**\n* Second").to_html(),
            expected_html_node.to_html()
        )

    def test_ordered_list_to_html_node(self):
        expected_html_node: ParentNode = ParentNode(
            tag="ol",
            children=[
                ParentNode(tag="li", children=[LeafNode(tag=None, value="First")], props=None),
                ParentNode(tag="li", children=[LeafNode(tag=None, value="Second")], props=None)
            ],
            props=None
        )
        self.assertEqual(
            ordered_list_block_to_html_node("1. First\n2. Second").to_html(),
            expected_html_node.to_html()
        )
        
    def test_ordered_list_to_html_node_bold_inline_element(self):
        expected_html_node: ParentNode = ParentNode(
            tag="ol",
            children=[
                ParentNode(tag="li", children=[LeafNode(tag="b", value="BOLD")], props=None),
                ParentNode(tag="li", children=[LeafNode(None, "Second")], props=None)
            ],
            props=None
        )
        self.assertEqual(
            ordered_list_block_to_html_node("1. **BOLD**\n2. Second").to_html(),
            expected_html_node.to_html()
        )

    def test_paragraph_block_to_html_node(self):
        expected_HTML_node: ParentNode = ParentNode(tag="p", children=[LeafNode(None, "Hey")], props=None)
        self.assertEqual(
            paragraph_block_to_html_node("Hey").to_html(),
            expected_HTML_node.to_html()
        )

    def test_paragraph_block_to_html_node_empty(self):
        expected_HTML_node: ParentNode = ParentNode(tag="p", children=[], props=None)
        self.assertEqual(
            paragraph_block_to_html_node("").to_html(),
            expected_HTML_node.to_html()
        )

    def test_paragraph_block_to_html_with_inline_bold_element(self):
        expected_HTML_node: ParentNode = ParentNode(tag="p", children=[LeafNode(None, "Hey "), LeafNode(tag="b", value="BOLD")], props=None)
        self.assertEqual(
            paragraph_block_to_html_node("Hey **BOLD**").to_html(),
            expected_HTML_node.to_html()
        )

    def test_paragraph_block_to_html_with_inline_bold_italic_elements(self):
        expected_HTML_node: ParentNode = ParentNode(tag="p", children=[LeafNode(None, "Hey "), LeafNode(tag="b", value="BOLD"), LeafNode(None, " "), LeafNode(tag="i", value="ITALIC")], props=None)
        self.assertEqual(
            paragraph_block_to_html_node("Hey **BOLD** *ITALIC*").to_html(),
            expected_HTML_node.to_html()
        )

if __name__ == "__main__":
    unittest.main()