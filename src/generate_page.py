from block_markdown import markdown_to_html_node
from extract_title import extract_title
import os
import pathlib

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path)
    markdown: str = markdown_file.read()
    markdown_file.close()
    template_file = open(template_path)
    template: str = template_file.read()
    template_file.close()
    markdown_html: str = markdown_to_html_node(markdown).to_html()
    title: str = extract_title(markdown)
    page: str = template.replace("{{ Title }}", title).replace("{{ Content }}", markdown_html)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    dest_file = open(dest_path, "w")
    dest_file.write(page)
    dest_file.close()

def generate_page_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    for dir in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, dir)):
            if pathlib.PurePath(dir).suffix == ".md":
                generate_page(os.path.join(dir_path_content, dir), template_path, os.path.join(dest_dir_path, f"{pathlib.PurePath(dir).stem}.html"))
        else:
            generate_page_recursive(os.path.join(dir_path_content, dir), template_path, os.path.join(dest_dir_path, dir))
