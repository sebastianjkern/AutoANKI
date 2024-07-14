from marko.helpers import MarkoExtension
from marko import inline

class NewPage(inline.InlineElement):
    pattern = r'\\newpage(.*?)'
    parse_children = True
    priority = 6

    def __init__(self, match):
        self.target = match.group(1)

class NewPageRendererMixin(object):
    def render_new_page(self, element):
        return "<div style=\"page-break-after: always;\"></div>"

NewPageRenderer = MarkoExtension(
    elements=[NewPage],
    renderer_mixins=[NewPageRendererMixin]
)
