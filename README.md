<span data-idom="views.header"/>

# <div style="display:flex;justify-content:center;">IDOM</div>

---

### It's React, but in Python

<!--

talking about IDOM

new Framework for building
full-stack, interactive, web applications
in pure Python

Plotly Dash
Streamlit
IPyWidgets
PyWebIO
others...

full disclosure I'm also creator of IDOM

-->


# Web App vs Website

<img src="https://github.com/rmorshea/talks/raw/idom-its-react-but-in-python/static/site-vs-app.png" style="height:550px" />


# Diversity of Languages

<table style="width:100%">
<thead>
  <tr style="font-size:3.5vmin">
    <th>Server</th>
    <th>Browser</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Python</td>
    <td>Javascript</td>
  </tr>
  <tr>
    <td>Go</td>
    <td>React</td>
  </tr>
  <tr>
    <td>C++</td>
    <td>Vue</td>
  </tr>
  <tr>
    <td>Rust</td>
    <td>Svelte</td>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
  </tr>
</tbody>
</table>


# UI Frameworks

---

### A history as it relates to Python

<!--

A history of what?

since that's what
aims to be

 -->


# IPython Notebook

<img src="https://github.com/rmorshea/talks/raw/idom-its-react-but-in-python/static/ipython-notebook.png" style="height:550px" />

<!--

Start with IPython Notebook

a browser-based interactive computing
environment for Python

came about around
~2010-2012

The browser was becoming the OS of the internet.

Python, being a backend language had to adapt.
to the changing landscape

To my mind

IPython Notebook was a leader in that area

and remains so today

in the form of
Jupyter Lab
and the "Jovian" ecosystem

part of the reason for that is...

-->


# IPyWidgets

<img src="https://github.com/rmorshea/talks/raw/idom-its-react-but-in-python/static/ipywidgets-interaction.gif" />

<!--

related project

~2012-2014

leveraged IPython Notebook APIs

to give Python bidirectional comms with Browser

thus, brought interactivity to Python
more than just a REPL

see example

ipywidgets
important part
of spuring Python's popularity
amongst scientists

allowed for creation of
interactive
computing tools
for non-engineers

scientists no longer had to make User Interfaces
for themselves or others
in order to make their work
more approachable
easier to analyze

since creation IPyWidgets
has become a UI framework
in its own right
as people have developed
more and more
widgets
for ecosystem

shifting gears
to JS UI frameworks

-->


# Javascript UI Frameworks


<!--

This is where the "React"
from the title
comes into the picture

How many have heard of React?

if you're unfamiliar don't wory.
part of the point
I don't want you need to know about
Javascript or React

getting back to it

-->


# A Paradigm Shift

<img src="https://github.com/rmorshea/talks/raw/idom-its-react-but-in-python/static/js-shift-to-declarative.png" />

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


# Imperative vs Declarative?

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
that being
details those transtions between states
of course
at the cost of control

but many times we don't want that burden
bugs
extra work

-->


# Wisdom of the Crowd

<img src="https://github.com/rmorshea/talks/raw/idom-its-react-but-in-python/static/js-shift-to-declarative.png" />

<!--

Now you can take me at my word here

or you can trust wisdom of the crowd

the popularity of React is quite decisive

 -->


#
<div>
  <h1>What About UI Frameworks</h1>
  <h1 style="display:flex;justify-content:center;">for Python?</h1>
</div>

<!--

What About Python UI Frameworks?
Have they learned the same lesson?

Declarative programs tends to be
easier to do correctly

unfortunately, no
not really

almost all
one form or another
fall prey problems of
imperative design patterns

there's been some movement in a possitive direction
Streamlit has done best
but doesn't fully embrace it
particularly with state

-->

<div style="width:100%">
  <div style="display:flex;justify-content:center;">
    <img style="width:30%;margin:7%" src="https://static.bokeh.org/branding/logos/bokeh-logo.svg" />
    <img style="width:30%;margin:7%" src="https://panel.holoviz.org/_static/logo_stacked.png" />
  </div>
  <div style="display:flex;justify-content:center;">
    <img style="width:30%;margin:7%" src="https://avatars.githubusercontent.com/u/5997976?s=200&v=4" />
    <img style="width:30%;margin:7%" src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg" />
  </div>
</div>

#

<img src="https://raw.githubusercontent.com/idom-team/idom/main/branding/svg/idom-logo.svg" />

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

to demonstrate the similarities
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

ReactDOM.render(
  <ClickCounter />,
  document.getElementById("root"),
);
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


# How Does It Work?

<!--

How does IDOM manage this

And why haven't other frameworks already done this

-->


# Model Synchronization

<div style="display:flex;justify-content:center;">
  <span data-idom="views.img" data-file="mvc-flow-diagram.svg" />
</div>


# View Synchronization

<div style="display:flex;justify-content:center;">
  <span data-idom="views.img" data-file="idom-flow-diagram.svg" />
</div>


#

<!--

virtual document object model

a.k.a. Virtual DOM

what is the DOM?

standardized data structure
which "models"
a "document"
as a series of nodes or "objects"
arranged in form of a tree

see image

-->

<div style="display:flex;justify-content:center">
  <h1 style="font-size:3vw;width:40%;margin-right:50px;border-right:solid 7px grey;">
    Virtual Document Object Model
  </h1>
  <img
    style="width:50%"
    src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/DOM-model.svg/1280px-DOM-model.svg.png"
  />
</div>


# Some HTML

```html
<div>
  Put your name here:
  <input
    type="text"
    minlength="4"
    maxlength="8"
    onchange="a_python_callback(event)"
  />
</div>
```

# Turned Into VDOM

```python
{
  "tagName": "div",
  "children": [
    "Put your name here:",
    {
      "tagName": "input",
      "attributes": {
        "type": "text",
        "minLength": 4,
        "maxLength": 8
      },
      "eventHandlers": {
        "onChange": {
          "target": "unique-id-of-a_python_callback",
          "preventDefault": False,
          "stopPropagation": False
        }
      }
    }
  ],
}
```

# Create VDOM With IDOM

```python
html.div(
  "Put your name here:",
  html.input(
    {
        "type": "text",
        "minLength": 4,
        "maxLength": 8,
        "onChange": lambda event: ...
    }
  )
)
```


#

> **Isn’t wiring a virtual representation of the view to the client,
> even if its diffed, expensive?**



#

<div style="height:45vh" />

<div>
<h1>What Can IDOM Do?</h1>
</div>

<div style="height:50vh" />

<!--

SCROLL DOWN!

But it also doesn't give up the things that are great about Python
MATPLOTLIB!

 -->

<span data-idom="views.gallery" />

<div style="height:25vh" />


# Javascript Integration

```python
import idom

victory = idom.web.module_from_template(
  "react", "victory-bar", fallback="⌛"
)
VictoryBar = idom.web.export(victory, "VictoryBar")

@idom.component
def MyBarChart():
    bar_style = {
        "parent": {"width": "500px"},
        "data": {"fill": "royalblue"},
    }
    return VictoryBar({"style": bar_style})
```

<div style="display:flex;justify-content:center;">
  <span data-idom="views.victory_chart" />
</div>


<!--



-->


# Demo
