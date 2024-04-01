import re

def extract_markdown_images(text: str):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches