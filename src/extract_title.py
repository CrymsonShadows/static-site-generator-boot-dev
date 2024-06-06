def extract_title(markdown: str) -> str:
    if markdown.startswith("# "):
        title: str = markdown.split("\n", 1)[0]
        title = markdown.lstrip("# ")
        return title
    else:
        raise Exception("No h1 header present for title")