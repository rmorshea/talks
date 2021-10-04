<span data-idom="views.header"/>

# <div style="display:flex;justify-content:center;"><a href="https://github.com/idom-team/idom" target="_blank">IDOM</a></div>

---

### It's React, but in Python

<!--

presenting on IDOM

new UI Framework for Python
best compared to

Plotly Dash
Streamlit
IPyWidgets
others...

full disclosure I'm also creator of IDOM

-->

# The Plan

- A bit of history
- Where IDOM fits in
- What you can do with IDOM
- How IDOM works


# UI Frameworks

---

### a *very* brief history...

#### ...as it relates to Python

<!--

A history of what?

given that IDOM is a UI framework

that's what we're gonna focus on

 -->


# IPython Notebook

<img src="https://github.com/rmorshea/talks/raw/master/idom/what-is-idom/static/ipython-notebook.png" style="height:550px" />

<!--

~2010-2012

The browser was becoming the OS of the internet.

Python, being a backend language had to adapt.

To my mind

IPython Notebook was a leader in that area

and remains so today

in the form of
Jupyter Lab
and the "Jovian" ecosystem

part of the reason for that is...

-->


# IPyWidgets

<img src="https://github.com/rmorshea/talks/raw/master/idom/what-is-idom/static/ipywidgets-interaction.gif" />

<!--

related project

~2012-2014

leveraged IPython Notebook APIs

to give Python bidirectional comms with Browser

thus, brought interactivity to Python

see example

This helped to spur Python's popularity amongst scientists

allowed for creation of
interactive
computing tools
for non-engineers

scientists no longer had to make User Interfaces themselves
in order to make their work more approachable

shifting gears...

-->


# Javascript UI Frameworks


<!--

This is where the "React"
from the title
comes into the picture

How many of you guys have heard of React?

if you're unfamiliar don't wory.
part of the point
I don't want you need to know about
Javascript or React

moving on

-->


# A Paradigm Shift

<img src="https://github.com/rmorshea/talks/raw/master/idom/what-is-idom/static/js-shift-to-declarative.png" />

<!--

a little later
2015-2017

paradigm shift
within world of Javascript UI Framework

new declarative frameworks
like React and Vue
gained popularity

over old imperative ones
like Angular
which had been extremely popular prior

While there are many fads in the JS world
declarative frameworks
and React specifically
seem to have staying power.

based on the graph
not going anywhere anytime soon

to understand why
need to talk about those two terms

-->


# Declarative vs Imperative?

<!--

high level
these terms
describe two programming paradigms

depending on context
what paradigm you're programming in

stylistic choice
one you might not even be aware you're making

or enforced by a framework or programming language

what is difference?

-->

# Imperative

<!--

what it means
to operate in imperative
with respect to making web applications

you as developer
are responsible for

-->

- Define state app evolves through
- and how it transitions

<!--

In short, you as the developer have very fine grained control

-->

# Declarative

- Only responsible for app states
- Transitions are handled for you


# Is Declarative Better?

<!--

So why are declarative JS frameworks
gaining market share?

may have noticed
in declarative

one less thing for programmer to worry about
of course
at the cost of control

but many times we don't want that burden
bugs
extra work

---

before moving on

important to state
there's a lot more to this topic

but for the purposes of this talk that's all you need to know

-->

# <div style="display:flex;justify-content:center;"><div>What About Python UI Frameworks?</div></div>

<!--

What About Python UI Frameworks?
Have they learned the same lesson?

Declarative programs tends to be
easier to do correctly


It's been a while since IPyWidgets

unfortunately, no
not really

almost all
one form or another
fall prey problems of
imperative design patterns

there's been some movement in a possitive direction
Streamlit has done best
but doesn't fully embrace it

-->

---

<div style="width:100%">
  <div style="display:flex;justify-content:center;">
    <img style="width:35%;margin:7%" src="https://static.bokeh.org/branding/logos/bokeh-logo.svg" />
    <img style="width:35%;margin:7%" src="https://panel.holoviz.org/_static/logo_stacked.png" />
  </div>
  <div style="display:flex;justify-content:center;">
    <img style="width:35%;margin:7%" src="https://avatars.githubusercontent.com/u/5997976?s=200&v=4" />
    <img style="width:35%;margin:7%" src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg" />
  </div>
</div>

#

<!--

That's where IDOM comes in

unlike peers
IDOM takes heavy inspiration from the React UI Framework

thus has many of the same declarative virtues

Beyond that though
IDOM as UI framework for Python is unusually powerful

because

puts nearly all the same capabilities of the React
into the hands of Python developers

which, mind you, React is a JS Framework
and having near parity
with features of a JS Framework
is pretty unheard of

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

want to
take a moment

To emphasize the inspriation from React

look at example

 -->

# Simple Click Counter

---

<div style="display:flex;justify-content:center;margin-top:50px;">
  <span data-idom="views.click_count" />
</div>


# With React

<!--

This is Javascript (JSX specifically)
so the syntax looks weird

just note a few things

-->

```jsx
import React, { useState } from "react";
import ReactDOM from "react-dom";

function ClickCounter() {
    const [count, setCount] = useState(0);
    return <button onClick={() => setCount(count + 1)}>
        clicked {count} times
    </button>;
}

ReactDOM.render(<ClickCounter />, document.getElementById("root"));
```


# With IDOM

```python
import idom

@idom.component
def ClickCounter():
    count, set_count = idom.hooks.use_state(0)
    return idom.html.button(
        {"onClick": lambda _: set_count(count + 1)},
        f"clicked {count} times"
    )

idom.run(Counter)
```

# Transferable Knowledge

<!--

A cool side effect
of similarity

When you learn how to write a app with IDOM

while not exactly the same

If you choose to learn Javascript
much of what you learned with IDOM
can be directly applied
writing apps with React in JS

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
