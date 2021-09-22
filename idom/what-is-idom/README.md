<span data-idom="views/header.py"/>

# <a href="https://github.com/idom-team/idom" target="_blank">IDOM</a> - it's React, but in Python

<!--

- say name
- IDOM stands for Interactive-DOM (Document Object Model)
- social and slide links at the end
- assumes some basic knowledge of:
  - HTML
  - web apps

-->


# Contents

- Definitions
- What is IDOM?



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

---

<div style="margin-left: 20%" >
  <span data-idom="views/click_count.py" />
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

    button.on_click = make_increment_callback(button)  # and here
    button.children = ["clicked 0 times"]  # also here

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


# Inspired by React?

<!--

The main thing we took are components and hooks

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

- component: encapsulates the state of representation of a view
- hook: allow you to "hook" into the life cycle and state of a component

- use_state hook achieves the same effect
- returns the current state with a callback to update it
- also defines a default value

-->


# Reworked With IDOM

```python
import idom

@idom.component
def click_count_button():
    count, set_count = idom.hooks.use_state(0)

    def increment_count(event):
        set_count(count + 1)

    return idom.html.button({"onClick": increment_count}, f"clicked {count} times")
```
