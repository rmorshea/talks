import time
import asyncio
import random
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
    .linked-inputs input {width: 48%;float: left; font-size: 20px; border: 1px solid grey}
    .linked-inputs input + input {margin-left: 4%}
    fieldset {padding: 3px; padding-bottom: 6px;}
    legend {background-color: #000; color: #fff; padding: 3px 6px; margin: 3px; font-size: 24px;}
    """)

    return idom.html.div(style, plot, mu_inputs, sigma_inputs)


@idom.element
async def Plot(self, x, y):
    fig, axes = plt.subplots(figsize=(8, 4))
    axes.plot(x, y)
    img = idom.Image("svg")
    fig.savefig(img.io, format="svg")
    plt.close(fig)
    model = await img.render()
    model["attributes"]["width"] = "100%"
    return model


def linked_inputs(label, value, *types, **attributes):
    var = idom.Var(value)

    inputs = []
    for t in types:
        inp = idom.Input(t, value, **attributes)

        @inp.events.on("change")
        async def on_change(inp):
            for i in inputs:
                i.update(inp.value)
            var.set(inp.value)

        inputs.append(inp)

    fs = idom.html.fieldset(idom.html.legend(label), *inputs, cls="linked-inputs")

    return var, fs
