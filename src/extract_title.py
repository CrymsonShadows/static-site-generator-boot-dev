def extract_title(markdown: str) -> str:
    if markdown.startswith("# "):
        end: str = markdown.find("\n")
        title: str = ""
        if end == -1:
            title = markdown.lstrip("# ")
        else:
            title = markdown[: end].lstrip("# ")
        return title
    else:
        raise Exception("No h1 header present for title")