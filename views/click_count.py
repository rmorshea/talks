import idom


@idom.component
def Main():
    count, set_count = idom.hooks.use_state(0)
    return idom.html.button(
        {
            "onClick": lambda _: set_count(count + 1),
            "style": {"fontSize": "2em"},
        },
        f"clicked {count} times",
    )
