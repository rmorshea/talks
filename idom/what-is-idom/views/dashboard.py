import time
import asyncio
import random
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


def main():
    return RandomWalk()


@idom.element
async def RandomWalk(self):
    x, y = [0] * 50, [0] * 50
    plot = Plot(x, y)

    mu_var, mu_inputs = linked_inputs(
        "Mean", 0, "number", "range", min=-1, max=1, step=0.01
    )
    sigma_var, sigma_inputs = linked_inputs(
        "Standard Deviation", 1, "number", "range", min=0, max=2, step=0.01
    )

    @self.animate(rate=0.3)
    async def walk(stop):
        x.pop(0)
        x.append(x[-1] + 1)
        y.pop(0)
        diff = random.gauss(float(mu_var.get()), float(sigma_var.get()))
        y.append(y[-1] + diff)
        plot.update(x, y)

    style = idom.html.style("""
    .linked-inputs {margin-bottom: 20px}
    .linked-inputs input {width: 48%;float: left}
    .linked-inputs input + input {margin-left: 4%}
    """)

    return idom.html.div(style, plot, mu_inputs, sigma_inputs, style={"width": "60%"})


@idom.element(run_in_executor=True)
async def Plot(self, x, y):
    fig, axes = plt.subplots()
    axes.plot(x, y)
    img = idom.Image("svg")
    fig.savefig(img.io, format="svg")
    plt.close(fig)
    return img


def linked_inputs(label, value, *types, **attributes):
    var = idom.Var(value)

    inputs = []
    for t in types:
        inp = idom.Input(t, value, **attributes)

        @inp.events.on("change")
        async def on_change(inp, event):
            for i in inputs:
                i.update(inp.value)
            var.set(inp.value)

        inputs.append(inp)

    fs = idom.html.fieldset(idom.html.legend(label), *inputs, cls="linked-inputs")

    return var, fs
