import idom


victory = idom.web.module_from_template("react", "victory-bar", fallback="⌛")
VictoryBar = idom.web.export(victory, "VictoryBar")


def main():
    return VictoryBar(
        {"style": {"parent": {"width": "500px"}, "data": {"fill": "royalblue"}}}
    )
