<span data-idom="views.header"/>

# <a href="https://github.com/idom-team/idom" target="_blank">IDOM</a> - it's React, but in Python

<!--
- not WS afiliated
- IDOM stands for Interactive-DOM (Document Object Model)
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

as part of this project to bring Python to the browser

IPyWidgets was created.

Allowed Python to have bidirectional comms with DOM and Javascript

used Notebook APIs

This helped to spur

-->


# Javascript


# Declarative Frameworks

<img src="https://github.com/rmorshea/talks/raw/master/idom/what-is-idom/static/js-shift-to-declarative.png" />


# What is React <a href="https://reactjs.org/" target="_blank"><i class="fab fa-react" /></a>?

- A Javascript library for building user interfaces
- which uses "declarative" design patterns

<!--

refer to title of talk "it's React"

ASK: "how many know React"
ASK: "how many know what declarative means"

no doubt many have heard, but also many probably haven't used
we're going to briefly touch on React before going deeper

-->

# Declarative vs Imperative?

- [declarative](https://en.wikipedia.org/wiki/Declarative_programming) - expresses the logic of a computation without describing its control flow.
- [imperative](https://en.wikipedia.org/wiki/Imperative_programming) - uses statements that change a program's state.

<!--

- according to wikipedia...

- means that:
  - describe state of app at each step
  - the programming framework handles transitions

- another way:
  - describe app in state A and B
  - on change: framework figures out how to get there

-->


# Give Me An Example

<div style="margin-left:20%;margin-top:50px;" >
  <span data-idom="views.click_count" />
</div>

<!--

shows interactive click count button

-->


# Imperative Style

```python
def click_count_button():
    state = {"count": 0}
    button = Button()

    def increment_count():
        state["count"] += 1
        button.children = [f"clicked {state['count']} times"]

    button.on_click = increment_count
    button.children = ["clicked 0 times"]

    return button
```


# Declarative Style


```python
def click_count_button():
    state: dict = current_state()
    count = state.get("count", 0)

    def increment_count():
        update_state({"count": count + 1})

    return Button({"on_click": increment_count}, f"clicked {count} times")
```


# Why Be Declarative?

- No clear static relations
- Referential links cause complexity
- Refactoring is difficult

<!--

- No one place to know structure and behavior of view.
- Callbacks must hold references to all the elements that they will update.
- Last is hard to ship without larger program

-->


# No Static Relations

```python
def click_count_button():
    state = {"count": 0}
    button = create_element("button")

    def increment_count():
        state["count"] += 1
        button.children = [f"clicked {state['count']} times"]  # here

    button.on_click = increment_count  # and here
    button.children = ["clicked 0 times"]  # also here

    return button
```

<!--

structure/behavior defined in more than one place

-->


# Bad Referential Links

```python
from some_other_module import make_increment_callback

def click_count_button():
    state = {"count": 0}
    button = create_element("button")

    button.on_click = make_increment_callback(button)
    #                 ^ defined in another module
    button.children = ["clicked 0 times"]

    return button
```

```python
# some_other_module.py

def make_increment_callback(button):

    def increment_count():
        state["count"] += 1
        button.children = [f"clicked {state['count']} times"]

    return another_callback_constructor(button)
```

<!--

imagine that we start to develop this
what if the increment callback became more complex
we might create some constructor for the callback
and move the constructor into another module
now description of view evolution is scattered across the callstack

-->


# What is IDOM?

- A Python library for building user interfaces
- which uses declarative design patterns inspired by React

<!--

Ok, now that we've got some context under out belt
what is IDOM?
Well hopefully these bullets make sense now.

-->


# How Did React Inspire It?

<!--

The main thing we took where the
- functional components
- hooks

-->


# Components and Hooks

Instead of:

```python
current_state: Callable[[], dict]
update_state: Callable[[dict], None]

def click_count_button():
    state = current_state()
    count = state.get("count", 0)
```

With IDOM we would write:

```python
import idom

@idom.component
def ClickCountButton():
    count, set_count = idom.hooks.use_state(0)
```

<!--

- component: encapsulates the state and representation of a view
- hook: allows you to "hook" into the life cycle and state of a component

- use_state hook achieves the same effect
- returns the current state with a callback to update it
- also defines a default value

-->


# Declarative Psuedo Code


```python
def click_count_button():
    state: dict = current_state()
    count = state.get("count", 0)

    def increment_count():
        update_state({"count": count + 1})

    return Button({"on_click": increment_count}, f"clicked {count} times")
```


# Code Written With IDOM

```python
import idom

@idom.component
def ClickCountButton():
    count, set_count = idom.hooks.use_state(0)

    def increment_count(event):
        set_count(count + 1)

    return idom.html.button({"onClick": increment_count}, f"clicked {count} times")
```


# Why IDOM?

- Declarative
- Empowers Python users
- Simple Javascript bindings
- Ecosystem independent

<!--

we got a sense for what it is

now why should you use it - there are lots of alternatives out there

most assume you have a JS team that can make custom components

Streamlit: state management is restrictive
IpyWidgets: imperative design patterns
complicated JS bindings



- declarative
  - already covered but its an important point
  - many peers rely on imperative design patterns

GO TO NEXT SLIDE

-->


# Empowers Python Users

<span data-idom="views.gallery" />

<!--

- IDOM doesn't limit Python users to high level abstractions
  - You can control the DOM with nearly as much flexibility as a JS dev

-->


# Javascript "Just Works"

```python
import idom

mui = idom.web.module_from_template("react", "@material-ui/core@^5.0", fallback="⌛")
Switch = idom.web.export(mui, "Switch")

@idom.component
def DayNightSwitch():
    state, set_state = idom.hooks.use_state(False)
    return idom.html.div(
        Switch({"checked": state, "onChange": lambda _, checked: set_state(checked)}),
        "🌞" if state else "🌚",
    )
```

<div style="margin-left: 30%">
  <span data-idom="views.day_night_switch" />
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


# How Does it Work?


# VDOM

<span data-idom="views.img" data-file="idom-flow-diagram.svg" />
