from marko.helpers import MarkoExtension
from marko import inline

class Image(inline.InlineElement):
    pattern = r'\[\[image: (.*?)\]\]'
    parse_children = True

    def __init__(self, match):
        self.target = match.group(1)

class ImageRendererMixin(object):
    def render_image(self, element):
        return  f"""
        <div style=\"display: flex; justify-content: space-evenly; flex-direction: row; align-items: center; break-inside: avoid;\">
            <figure>
                <img src="{element.target}"/>
                <figcaption>This is a graph</figcaption>
            </figure>
        </div>
        """

ImageRenderer = MarkoExtension(
    elements=[Image],
    renderer_mixins=[ImageRendererMixin]
)
