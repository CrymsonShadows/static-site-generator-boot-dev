from htmlnode import LeafNode
from extractlink import exttract_markdown_links, extract_markdown_images

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text: str, text_type: str, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception(f"Unknown text type: {text_node.text_type}")
    
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_old_nodes = old_node.text.split(delimiter)
        split_nodes = []
        if len(split_old_nodes) % 2 == 0:
            raise ValueError("Invalid Markdown syntax, imbalanced section")
        for i in range(len(split_old_nodes)):
            if split_old_nodes[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_old_nodes[i], text_type_text))
            else:
                split_nodes.append(TextNode(split_old_nodes[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text == "":
            continue
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        text_left = old_node.text
        for img_tup in images:
            split_text = text_left.split(f"![{img_tup[0]}]({img_tup[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(img_tup[0], text_type_image, img_tup[1]))
            text_left = split_text[1]
        if text_left != "":
            new_nodes.append(TextNode(text_left, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text == "":
            continue
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        links = exttract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        text_left = old_node.text
        for link_tup in links:
            split_text = text_left.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
            text_left = split_text[1]
        if text_left != "":
            new_nodes.append(TextNode(text_left, text_type_text))
    return new_nodes

def text_to_textnodes(text: str):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes