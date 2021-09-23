from pathlib import Path
import idom


PROJECT_DIR = Path(__file__).parent.parent


def main(file: str, style: str = ""):
    style_dict = {}
    for style_part in map(str.strip, style.split(";")):
        if not style_part:
            continue
        name, value = list(map(str.strip, style_part.split(":")))
        name = name.title().replace("-", "")
        name = name[0].lower() + name[1:]
        style_dict[name] = value

    file_path = PROJECT_DIR / "static" / file

    return idom.widgets.image(
        file_path.suffix[1:],
        file_path.read_text(),
        {"style": style_dict},
    )
