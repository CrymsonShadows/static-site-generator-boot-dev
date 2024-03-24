class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        attr = ""
        if self.props is None:
            return attr
        for key, val in self.props.items():
            attr += f' {key}="{val}"'
        return attr

    def __repr__(self):
        return f'HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

