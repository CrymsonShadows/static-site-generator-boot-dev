from copy_static import copy_static
from generate_page import generate_page_recursive

def main():
    copy_static()
    generate_page_recursive("content", "template.html", "public")

main()