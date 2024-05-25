from htmlnode import HTMLNode, ParentNode
from textnode import TextNode, text_to_textnodes, text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown: str):
    lines = markdown.split("\n\n")
    blocks: list[str] = []
    blocks = map(lambda line: line.strip(), lines)
    blocks = list(filter(lambda block: block != "", blocks))
    return blocks

def block_to_block_type(block: str):
    # Heading
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    # Code
    if block.startswith("```") and block.endswith("```") and len(block) != 3:
        return block_type_code
    lines: list[str] = block.split("\n")
    # Quote
    every_line_char_start = True
    for line in lines:
        if line.startswith(">") != True:
            every_line_char_start = False
            break
    if every_line_char_start == True:
        return block_type_quote
    # Unordered List
    every_line_char_start = True
    for line in lines:
        if line.startswith("*") != True and line.startswith("-") != True:
            every_line_char_start = False
            break
    if every_line_char_start == True:
        return block_type_unordered_list
    # Ordered List
    num = 1
    every_line_char_start = True
    for line in lines:
        if line.startswith(f"{num}.") != True:
            every_line_char_start = False
            break
        num += 1
    if every_line_char_start == True:
        return block_type_ordered_list
    return block_type_paragraph

def quote_block_to_html_node(block: str) -> HTMLNode:
    lines: str = block.splitlines()
    lines = list(map(lambda line: line.lstrip("> "), lines))
    cleaned_block = "<br>".join(lines)
    text_nodes: list[TextNode] = text_to_textnodes(cleaned_block)
    html_nodes: list[HTMLNode] = list(map(text_node_to_html_node, text_nodes))
    quote_html_node: ParentNode = ParentNode(tag="blockquote", children=html_nodes, props=None)
    return quote_html_node

def unordered_list_block_to_html_node(block: str) -> HTMLNode:
    lines: str = block.splitlines()
    lines = list(map(lambda line: line[2:], lines))
    list_items: list[HTMLNode] = []
    for line in lines:
        text_nodes: list[TextNode] = text_to_textnodes(line)
        html_nodes: list[HTMLNode] = list(map(text_node_to_html_node, text_nodes))
        list_item: ParentNode = ParentNode(tag="li", children=html_nodes, props=None)
        list_items.append(list_item)
    unordered_list: ParentNode = ParentNode(tag="ul", children=list_items, props=None)
    return unordered_list

def ordered_list_block_to_html_node(block: str) -> HTMLNode:
    lines: str = block.splitlines()
    lines = list(map(lambda line: line[line.find(".") + 2:], lines))
    list_items: list[HTMLNode] = []
    for line in lines:
        text_nodes: list[TextNode] = text_to_textnodes(line)
        html_nodes: list[HTMLNode] = list(map(text_node_to_html_node, text_nodes))
        list_item: ParentNode = ParentNode(tag="li", children=html_nodes, props=None)
        list_items.append(list_item)
    ordered_list: ParentNode = ParentNode(tag="ol", children=list_items, props=None)
    return ordered_list

def code_block_to_html_node(block: str) -> HTMLNode:
    lines: str = block.splitlines()
    lines = list(map(lambda line: line.lstrip("`"), lines))
    lines = list(map(lambda line: line.rstrip("`"), lines))
    cleaned_block = "<br>".join(lines)
    text_nodes: list[TextNode] = text_to_textnodes(cleaned_block)
    html_nodes: list[HTMLNode] = list(map(text_node_to_html_node, text_nodes))
    code_html_node: ParentNode = ParentNode(tag="code", children=html_nodes, props=None)
    pre_html_node: ParentNode = ParentNode(tag="pre", children=[code_html_node], props=None)
    return pre_html_node

def heading_block_to_html_node(block: str) -> HTMLNode:
    heading: str = ""
    if block.startswith("######"):
        heading = "h6"
    elif block.startswith("#####"):
        heading = "h5"
    elif block.startswith("####"):
        heading = "h4"
    elif block.startswith("###"):
        heading = "h3"
    elif block.startswith("##"):
        heading = "h2"
    elif block.startswith("#"):
        heading = "h1"
    line: str = block.lstrip("# ")
    text_nodes: list[TextNode] = text_to_textnodes(line)
    html_nodes: list[HTMLNode] = list(map(text_node_to_html_node, text_nodes))
    heading_html_node: ParentNode = ParentNode(tag=heading, children=html_nodes, props=None)
    return heading_html_node

def paragraph_block_to_html_node(block: str) -> HTMLNode:
    text_nodes: list[TextNode] = text_to_textnodes(block)
    html_nodes: list[HTMLNode] = list(map(text_node_to_html_node, text_nodes))
    paragraph_html_node: ParentNode = ParentNode(tag="p", children=html_nodes, props=None)
    return paragraph_html_node