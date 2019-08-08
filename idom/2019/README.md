<div alt="python:views/header.py"/>

# iDOM

- <a href="https://github.com/rmorshea/idom">
  <i class="fas fa-code-branch"></i>
  github.com/rmorshea/idom
</a>

- a framework for controlling the web with Python


<div alt="python:views/logo.py"/>


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

- A Python dev tool to make interactive webpages.

- A JSON protocol for server-side rendering HTML.

- An easy way to integrate existing JS libraries.

- Not a Jupyter Widget


# A Simple Slideshow

<img src="https://picsum.photos/800/300" border="7" alt="python:views/example.py"/>


# The Slideshow Code

```python
import idom

@idom.element
async def Slideshow(self, index=0):
    events = idom.Events()

    @events.on("click")
    async def change():
        self.update(index + 1)

    return idom.html.img(
      src=f"https://picsum.photos/800/300?image={index}",
      style={"border": "7px solid grey"},
      eventHandlers=events,
    )

idom.server.sanic.PerClientState(Slideshow).run("localhost", 8765)
```


# So How Does It Work?

1. The server renders a Document Object Model (DOM)
2. A websocket transmits that model to the client.
3. The browser interprets the model and displays it.
4. A user interacts with the view and triggers an event.
5. The websocket transmits the event to the server.
6. Repeat...


# Why?

- Learning and keeping up with Javascript is hard
- Python has very few libraries for creating GUIs

### Why Not Widgets?

- Jupyter Widgets are bound to the Jupyter ecosystem
- In order to develop them you need to know Javascript


# What Can It Do?

- Dashboards
- Websites
- Games (simple ones)
- Desktop apps (Electron JS)
- **This slide deck!**


# A Simple Dashboard

<img
  src="https://github.com/rmorshea/talks/raw/master/idom/2019/static/dashboard.gif"
  alt="python:views/dashboard.py"
/>


# Future Work

- Ability to integrate existing 3rd party JS libraries
- Create an Electron JS wrapper for iDOM
- Include bindings for other backend servers
- Improve test coverage and documentation
- Finalize communication specification
- Performance improvements (JSON compression)


# End

**These Slides**:
<a href="https://github.com/rmorshea/talks/tree/master/idom/2019-06-Paris">
  <i class="fas fa-file-powerpoint"></i>
  github.com/rmorshea/talks
</a>

<table>
  <tr>
    <td>
      <a href="https://github.com/rmorshea/idom">
        <i class="fas fa-code-branch"></i>
        github.com/rmorshea/idom
      </a>
    </td>
  </tr>
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
