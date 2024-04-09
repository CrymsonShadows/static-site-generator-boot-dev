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
    blocks = list(filter(lambda block: not block == "", blocks))
    return blocks

def block_to_block_type(block: str):
    # Heading
    if block.startswith(("#", "##", "###", "####", "#####", "######")):
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