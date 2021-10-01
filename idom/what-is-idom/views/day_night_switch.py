import idom


mui = idom.web.module_from_template("react", "@material-ui/core@^5.0", fallback="⌛")
Switch = idom.web.export(mui, "Switch")


@idom.component
def Main():
    state, set_state = idom.hooks.use_state(False)
    return idom.html.div(
        idom.html.div(
            {"style": {"display": "inline-block"}},
            Switch(
                {"checked": state, "onChange": lambda _, checked: set_state(checked)}
            ),
        ),
        "🌞" if state else "🌚",
    )
