<span data-idom="views.header"/>

# <div style="display:flex;justify-content:center;"><a href="https://github.com/idom-team/idom" target="_blank">IDOM</a></div>

---

### It's React, but in Python

<!--
- not WS afiliated
- IDOM stands for Interactive-DOM (Document Object Model)
- bringing the declarative philosphy of react to Python
- social and slide links at the end

-->

# A Bit of History


# IPython Notebook

<img src="https://github.com/rmorshea/talks/raw/master/idom/what-is-idom/static/ipython-notebook.png" style="height:550px" />

<!--

~2010-2012

The browser was becoming the OS of the internet.

Python, being a backend language had to adapt.

To my mind

That happened first and foremost

with the IPython Notebook, now Jupyter

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

make interactive tools for non-engineers

-->


# Javascript Frameworks


# A Paradigm Shift

<img src="https://github.com/rmorshea/talks/raw/master/idom/what-is-idom/static/js-shift-to-declarative.png" />

<!--

2015-2017 new declarative Javascript frameworks gained popularity

Old imperative frameworks like Angular quickly went out of fashion

While there are many fads in the JS world declarative frameworks
and React specifically seem to have staying power.

to understand why
need to talk about what it means
to be imperative vs declarative

-->


# Declarative vs Imperative?

<!--

high level

these are two different programming paradigms
depending on context
whether working in declarative vs imperative is
- stylistic choice
- or enforced by a framework or programming language

what is difference?

-->

# Imperative

<!--

if talking about web apps

- imperative
  - define states the app evolves through
  - and details of how it transitions between those states
-->

# Declarative

<!--

- declarative:
  - still responsible describe state of app at each step
  - the programming framework handles transitions

Why is that better?

one less thing for programmer to worry about

important to state
there's a lot more to this topic

declarative is not always better
visa versa

but for the purposes of this talk that's all you need to know

-->

# <div style="display:flex;justify-content:center;"><div>What About Python UI Frameworks?</div></div>

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

after IPyWidgets?

unfortunately
have not adopt the lessons that were learned by Javascript frameworks like React
that made them popular and easy to use

that is, many fall prey to the problems of imperative design patterns in one form or another

-->


#

<!--

enter IDOM

IDOM takes heavy inspiration from React
specifically

thus has many of the same declarative virtues

Beyond that though
IDOM as UI framework for Python is unusually powerful

because

puts nearly all the same capabilities of the React framework into the hands
of Python developers

SCROLL DOWN!

But it also doesn't give up the things that are great about Python
MATPLOTLIB!

 -->

<div style="height:25vh" />

<img src="https://raw.githubusercontent.com/idom-team/idom/main/branding/svg/idom-logo.svg" />

<div style="height:50vh" />

---

<span data-idom="views.gallery" />


# Inspired By React

<!--

To emphasize the inspriation from React

look at example

 -->

# Simple Click Counter

---

<div style="display:flex;justify-content:center;margin-top:50px;">
  <span data-idom="views.click_count" />
</div>


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

# Transferable Knowledge

<!--

When you learn how to write a app with IDOM

while not exactly the same

If you choose to learn Javascript
much of what you learned with IDOM
can be directly applied to writing them in React

 -->


# But Wait... There's More!


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

When you do need to use Javascript it's easy

Because IDOM is still running Python in the backened
e.g. Matplotlib ex

So long as library you want is React

Just export the component you want and use it

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
