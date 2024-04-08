def markdown_to_blocks(markdown: str):
    lines = markdown.split("\n\n")
    blocks: list[str] = []
    blocks = map(lambda line: line.strip(), lines)
    blocks = list(filter(lambda block: not block == "", blocks))
    return blocks