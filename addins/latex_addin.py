import latex2mathml.converter
from marko.helpers import MarkoExtension
from marko import inline

class InlineLatex(inline.InlineElement):
    pattern = r'\$(.*?)\$'
    parse_children = True
    priority = 6

    def __init__(self, match):
        self.target = match.group(1)

class InlineLatexRendererMixin(object):
    def render_inline_latex(self, element):
        return latex2mathml.converter.convert(element.target)

InlineLatexRenderer = MarkoExtension(
    elements=[InlineLatex],
    renderer_mixins=[InlineLatexRendererMixin]
)
