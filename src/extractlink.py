import re

def extract_markdown_images(text: str):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def exttract_markdown_links(text: str):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches