from marko.helpers import MarkoExtension
from marko import inline

from sympy import symbols
from numpy import linspace
from sympy import lambdify
from sympy import parse_expr

import matplotlib.pyplot as plt
from io import StringIO

class Graph(inline.InlineElement):
    pattern = r'\[\[graph:(.*?)\]\]'
    parse_children = True

    def __init__(self, match):
        self.target = match.group(1)

class GraphRendererMixin(object):
    def render_graph(self, element):
        x = symbols('x')
        lam_x = lambdify(x, parse_expr(element.target), modules=['numpy'])

        x_vals = linspace(0, 10, 100)
        y_vals = lam_x(x_vals)

        plt.plot(x_vals, y_vals)
        plt.ylabel(f"${element.target}$")
        plt.xlabel("$x$")

        i = StringIO()
        plt.savefig(i, format="svg")
        
        return  f"""
        <div style=\"display: flex; justify-content: space-evenly; flex-direction: row; align-items: center; break-inside: avoid;\">
            <figure>
                <div>{i.getvalue()}</div>
                <figcaption>This is a graph</figcaption>
            </figure>
        </div>
        """

GraphRenderer = MarkoExtension(
    elements=[Graph],
    renderer_mixins=[GraphRendererMixin]
)
