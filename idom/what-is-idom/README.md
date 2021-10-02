<span data-idom="views.header"/>

# <div style="display:flex;justify-content:center;"><a href="https://github.com/idom-team/idom" target="_blank">IDOM</a></div>

---

### It's React, but in Python

<!--
- not WS afiliated
- IDOM stands for Interactive-DOM (Document Object Model)
- bringing declarative philosphy of react to Python
- social and slide links at the end

-->

# A Bit of History


# IPython Notebook

<img src="https://github.com/rmorshea/talks/raw/master/idom/what-is-idom/static/ipython-notebook.png" style="height:550px" />

<!--

~2010-2012

The browser was becoming the OS of the internet.

Python, being a backend language had to adapt.

Did so in the form of the IPython Notebook, now Jupyter

-->


# IPyWidgets

<img src="https://github.com/rmorshea/talks/raw/master/idom/what-is-idom/static/ipywidgets-interaction.gif" />

<!--

~2012-2014

as part of this project to bring Python to the browser

IPyWidgets was created.

Allowed Python to have bidirectional comms with DOM and Javascript

used Notebook APIs

This helped to spur Python's popularity amongst scientists

-->


# Javascript Frameworks


# A Paradigm Shift

<img src="https://github.com/rmorshea/talks/raw/master/idom/what-is-idom/static/js-shift-to-declarative.png" />

<!--

2015-2017 new declarative Javascript frameworks gained popularity

Old imperative frameworks like Angular quickly went out of fashion

While there are many fads in the JS world declarative frameworks
and React specifically seem to have staying power.

Why though?

-->


# Declarative vs Imperative?

- [imperative](https://en.wikipedia.org/wiki/Imperative_programming) - uses statements that change a program's state.
- [declarative](https://en.wikipedia.org/wiki/Declarative_programming) - expresses the logic of a computation without describing its control flow.

<!--

- according to wikipedia...

- means that:
  - describe state of app at each step
  - the programming framework handles transitions

Why is that better?

one less thing for programmer to worry about

-->


# Circling Back


# <div style="display:flex;justify-content:center;"><div>Python UI Frameworks</div></div>

---

<div style="width:100%">
  <div style="display:flex;justify-content:center;">
    <img style="width:35%;margin:7%" src="https://static.bokeh.org/branding/logos/bokeh-logo.svg" />
    <img style="width:35%;margin:7%" src="https://panel.holoviz.org/_static/logo_stacked.png" />
  </div>
  <div style="display:flex;justify-content:center;">
    <img style="width:35%;margin:7%" src="https://github.com/rmorshea/talks/raw/master/idom/what-is-idom/static/ipy-logo.png" />
    <img style="width:35%;margin:7%" src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg" />
  </div>
</div>

<!--

Bokeh
Panel
IPyWidgets
Streamlit

fall prey to the same problems that plague imperative UI JS frameworks like Angular

 -->


#

<div style="height:25vh" />

<img src="https://raw.githubusercontent.com/idom-team/idom/main/branding/svg/idom-logo.svg" />

<div style="height:50vh" />

---

<span data-idom="views.gallery" />


<!--

IDOM is a powerful UI framework

-->

# It's Declarative


# With React

```jsx
import React, { useState } from "react";
import ReactDOM from "react-dom";

function Counter() {
    const [count, setCount] = useState(0);
    return <button onClick={() => setCount(count + 1)}>
        clicked {count} times
    </button>;
}

ReactDOM.render(<Counter />, document.getElementById("root"));
```


# With IDOM

```python
import idom

@idom.component
def Counter():
    count, set_count = idom.hooks.use_state(0)
    return idom.html.button(
        {"onClick": lambda _: set_count(count + 1)},
        f"clicked {count} times"
    )

idom.run(Counter)
```

---

<div style="display:flex;justify-content:center;">
  <span data-idom="views.click_count" />
</div>


# Javascript "Just Works"

```python
import idom

victory = idom.web.module_from_template("react", "victory-bar", fallback="⌛")
VictoryBar = idom.web.export(victory, "VictoryBar")

@idom.component
def MyBarChart():
    bar_style = {"parent": {"width": "500px"}, "data": {"fill": "royalblue"}}
    return VictoryBar({"style": bar_style})
```

<div style="display:flex;justify-content:center;">
  <span data-idom="views.victory_chart" />
</div>


<!--

- When you do need to use Javascript it's easy
  - When you're just experimenting, many things work "out of the box"
  - When you it to be "production-grade" the bindings are simple
  - It's so simple you can do it without build tooling!

-->


# Ecosystem Independence

<span data-idom="views.img" data-file="idom-in-jupyter.gif" />

<!--

- IDOM's peers intentionally or by neccessity lock you into using one set of tools
  - EX. Jupyter Widgets, Plotly, or Streamlit
  - A widget written for one of these tools can't be ported elsewhere
  - One written for IDOM can, in principle be taken anywhere
  - Already supports Juyterpy and Plotly Dash

-->
