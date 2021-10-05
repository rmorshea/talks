
# Simple Javascript Bindings

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




# How Does it Work?


# VDOM

<span data-idom="views.img" data-file="idom-flow-diagram.svg" />






# Give Me An Example

<div style="margin-left:20%;margin-top:50px" >
  <span data-idom="views.click_count" />
</div>


# Imperative Style

```python
def make_click_count_button():
    state = {"count": 0}
    button = Button()

    def increment_count():
        state["count"] += 1
        button.children = [f"clicked {state['count']} times"]

    button.on_click = increment_count
    button.children = ["clicked 0 times"]

    return button
```


# No Clear Static Relations

```python
def make_click_count_button():
    state = {"count": 0}
    button = create_element("button")

    def increment_count():
        state["count"] += 1
        button.children = [f"clicked {state['count']} times"]  # <--- Here

    # And here
    # vvvvvvvv
    button.on_click = increment_count
    button.children = ["clicked 0 times"]

    return button
```

<!--

structure/behavior defined in more than one place

No one place to know structure and behavior of view.

-->


# Referential Links Are Bad

```python
from some_other_module import on_click_handler

def make_click_count_button():
    state = {"count": 0}
    button = create_element("button")

    add_on_click_handler(state, button)
    #                    ^^^^^  ^^^^^^
    #                    Must be passed around
    button.children = ["clicked 0 times"]

    return button
```

---

```python
def add_on_click_handler(state, button):

    def increment_count():
        # Mutates the state and view
        state["count"] += 1
        button.children = [f"clicked {state['count']} times"]

    button.on_click = increment_count
```

<!--

elements and state must be passed up and down the call stack wherever they are needed.

evolving view requires mutation

means that a function layers down in the call stack
can accidentally or intentionally impact the behavior of
ostensibly unrelated parts of the program.

-->


# Declarative Style

```python
def click_count_button():
    state: dict = current_state()
    count = state.get("count", 0)

    def increment_count():
        update_state({"count": count + 1})

    return Button({"on_click": increment_count}, f"clicked {count} times")
``` -->
