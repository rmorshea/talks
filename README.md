<span data-idom="views.header"/>

# <div style="display:flex;justify-content:center;">IDOM</div>

---

### It's React, but in Python

<!--

IDOM
of which I'm the creator

new Framework for building
full-stack, interactive, web applications
in pure Python

best compared to...

Plotly Dash
Streamlit
PyWebIO
others...

-->


# A Bit of History

<!--

before dive into things
bit of history
give some insite into why
created IDOM

gonna start by...

 -->


# IPython Notebook

<img src="https://github.com/rmorshea/talks/raw/idom-its-react-but-in-python/static/ipython-notebook.png" style="height:550px" />

<!--

a browser-based interactive computing
environment for Python

came to popularity
~2010-2012

and remains popular so today

in the form of
Jupyter Lab
and the "Jovian" ecosystem

part of the reason its still popular...

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

scientists no longer had to
learn Javascript
to make User Interfaces
for themselves or others
in order to make their work
more approachable
easier to analyze

since creation
IPyWidgets
has become a UI framework
in its own right
through tool Viola
strips away notebook interface
only show cell outputs

-->


#

<!--

since then
spoiled for choice
in space of
python-based user interface frameworks

bokeh
panel
streamlit
dash

others...

before we get too excited
about this progress

take a step
focus on what these frameworks can do better
because many suffer
from similar set of problems

want to do that
by looking at...

 -->

<div style="display:flex;justify-content:center;">
  <h1>Spoiled for Choice</h1>
</div>

---

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


# Javascript UI Frameworks


<!--

js frameworks over same time period...

This is where the "React"
from the title
comes into the picture

get a sense for familiarity...
Have heard of React?
Have used React?
Use it daily/weekly?

if you're unfamiliar don't wory.
part of the point
I don't want you need to know about
Javascript or React

just want to explain what it gets right
about UI frameworks in general

and how that informed development of IDOM

-->


# A Paradigm Shift

<img src="https://github.com/rmorshea/talks/raw/idom-its-react-but-in-python/static/js-shift-to-declarative.png" />

<!--

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


#
<div style="display:flex;justify-content:center;">
  <h1>What About in Python?</h1>
</div>

<!--

So going back to Python UI frameworks

Have they learned the same lesson?

Declarative programs tends to be
easier to do correctly

unfortunately, no
not really

all
one form or another
fall prey problems of
imperative design patterns

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

why should we care?
well as example


SCROLL DOWN!

all following were implemented in pure python
without writing any custom JS

what JS is used works "out of the box"
without any extra install/build steps
will talk a bit about that later

victory charting library
pigeon mapping tool
basic HTML
from scrath

...and as may have been guessing
even these slides were made with IDOM


But it also doesn't give up the things that are great about Python
MATPLOTLIB!

-->

<div style="height:27vh" />
<img src="https://raw.githubusercontent.com/idom-team/idom/main/branding/svg/idom-logo.svg" />
<div style="height:50vh" />

<span data-idom="views.gallery" />

<div style="height:25vh" />


#

<span data-idom="views.editor" />


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


# How Does It Work?

<!--

How does IDOM manage this

And why haven't other frameworks already done this

comes down to their general architectures

-->


# Model Synchronization

<!--

IDOM's peers go a route of

synchronizing a model,
which represents underlying state of app,
between server client
where client translates that model into a view
that is displayed to user

when user interacts with view
client sends event back to server
server updates the model
and the model gets resynced

the problem here
if our goal is to empower Python users
is that responsibilities are divided
between server/client

server responsible for updating model
the client responsible for translating model into view

-->

<div style="display:flex;justify-content:center;">
  <span data-idom="views.img" data-file="mvc-flow-diagram.svg" />
</div>


# View Synchronization

<!--

IDOM takes different approach
synchronizes representation of view
known as VDOM
(won't get into, could be whole other talk)
between server and client

as a result,
the server, and thus the Python developer
gains control over translating the model into the view

the specific implementation here shows that
things known as "components"
reusuable functions for contructing a part of the view
are composed together to create the whole view

for ex, click counter from before was a "component"

something called
a "layout" takes that representation of the view,
checks what's changed
sends the difference to the client
client then uses that diff to synchronize its
representation of the view

the user can the interact
the components re-render and thus the cycle starts again
 -->

<div style="display:flex;justify-content:center;">
  <span data-idom="views.img" data-file="idom-flow-diagram.svg" />
</div>


# Ecosystem Independence

<!--

Last thing want to touch on


 -->


#

<img src="https://raw.githubusercontent.com/idom-team/idom/main/branding/svg/idom-logo.svg" />

#

<h3><i class="fab fa-github" /> github.com/idom-team/idom</h3>
<h3><i class="fab fa-twitter" /> twitter.com/rmorshea</h3>
