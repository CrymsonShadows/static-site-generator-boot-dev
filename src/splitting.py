from block_markdown import markdown_to_blocks, block_to_block_type, block_type_paragraph, block_type_heading, block_type_code, block_type_quote, block_type_unordered_list, block_type_ordered_list, paragraph_block_to_html_node, quote_block_to_html_node
from htmlnode import ParentNode, LeafNode

block: str = "> First line\n> Second line "
lines: list[str] = block.splitlines()
lines = list(map(lambda line: line.lstrip("> "), lines))
block = "\n".join(lines)
print(block)

expected_HTML_node: ParentNode = ParentNode(tag="blockquote", children=[LeafNode(tag="blockquote", value="This is within a blockquote")], props=None)
print(f"quote_block_to_html_node: {quote_block_to_html_node("> This is within a blockquote").to_html()}")
print(f"expected_HTML_node: {expected_HTML_node.to_html()}")