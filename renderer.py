from pyhtml2pdf import converter
import os

from marko import Markdown

from addins.latex_addin import InlineLatexRenderer
from addins.graph_addin import GraphRenderer
from addins.image_addin import ImageRenderer
from addins.pagebreak_adding import NewPageRenderer

markdown = Markdown(extensions=['toc', NewPageRenderer, InlineLatexRenderer, GraphRenderer, ImageRenderer])

with open("README.md", "r") as file:
    try:
        os.mkdir("out")
    except:
        pass
    with open("out/output.html", "w") as out:
        content = markdown(file.read())
        toc = markdown.renderer.render_toc()
        out.write("<html style=\"font-family: sans-serif; font-size: 12pt;\"><div style=\"page-break-after: always;\"><h1>Table of Contents</h1>" + toc + "</div>" + content + "</html>")

path = os.path.abspath('out/output.html')
converter.convert(f'file:///{path}', 'out/output.pdf')