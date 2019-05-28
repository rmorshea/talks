<div alt="python:views/header.py"/>

# iDOM

A framework for controlling the web with Python

<img src="https://raw.githubusercontent.com/rmorshea/talks/master/idom/2019-06-Paris/static/logo.png" alt="python:views/logo.py"/>

<a href="https://github.com/rmorshea/idom">
  <i class="fas fa-code-branch"></i>
  github.com/rmorshea/idom
</a>


# About Me

<table>
  <tr>
    <td>
      <a href="https://rmorshea.github.io">
        <i class="fas fa-user"></i>
        Ryan Morshead
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://twitter.com/rmorshea">
        <i class="fab fa-twitter-square"></i>
        twitter.com/rmorshea
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/rmorshea">
        <i class="fab fa-github-square"></i>
        github.com/rmorshea
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="mailto:ryan.morshead@gmail.com">
        <i class="fas fa-envelope"></i>
        ryan.morshead@gmail.com
      </a>
    </td>
  </tr>
</table>


# What Is iDOM?

- A set of Python and Javascript libraries.

- A JSON protocol for server-side rendering HTML.

- A Python dev tool to make interactive webpages.

- An easy way for Javascript devs to empower them.


# A Quick Example

```python
import idom

@idom.element
async def Slideshow(self, index=0):
    events = idom.Events()

    @events.on("click")
    def change():
        self.update(index + 1)

    url = f"https://picsum.photos/800/300?image={index}"
    return idom.node("img", src=url, eventHandlers=events)

idom.server.sanic.PerClientState(Slideshow).run("localhost", 8765)
```


# The Result

<div alt="python:views/example.py"/>


# So How Does It Work?

1. The server renders a Document Object Model (DOM)
2. A websocket transmits that model to the client.
3. The browser interprets the model and displays it.
4. A user interacts with the view and triggers an event.
5. The websocket transmits the event to the server.
6. Repeat...


# Why?

- Learning and keeping up Javascript is hard
- Python has very few libraries for creating GUIs

### Why Not Widgets?

- Jupyter Widgets are bound to the Jupyter ecosystem
- In order to develop them you need to know Javascript


# What Can It Do?

- Dashboards
- Games (simple ones)
- Websites
- Desktop Apps
- This slide deck!


# A Simple Dashboard

<div alt="python:views/dashboard.py"/>
