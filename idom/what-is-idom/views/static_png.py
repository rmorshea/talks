import idom


@idom.component
def Main(file: str, style: str):
    style_dict = {}
    for style_part in map(str.strip, style.split(";")):
        if not style_part:
            continue
        name, value = list(map(str.strip, style_part.split(":")))
        name = name.title().replace("-", "")
        name = name[0].lower() + name[1:]
        style_dict[name] = value
    with open(f"static/{file}.png", "rb") as f:
        return idom.widgets.image("png", f.read(), {"style": style_dict})
