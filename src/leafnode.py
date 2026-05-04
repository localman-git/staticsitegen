from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value or self.value is None:
            raise ValueError
        
        if not self.tag or self.tag is None:
            return 'value'
        
        if self.props or self.props != None:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
        return f'<{self.tag}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'