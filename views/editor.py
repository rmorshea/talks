from pathlib import Path
import idom


file = Path(__file__).parent / "editor.js"
editor_module = idom.web.module_from_file("editor", file, fallback="...")
Editor = idom.web.export(editor_module, "Editor")


def main():
    content, set_content = idom.hooks.use_state(None)

    if content is not None:
        old_run = idom.run
        try:
            variables = {}
            output = idom.Ref(None)
            idom.run = output.set_current
            exec(content, variables)
        except Exception as err:
            result = idom.html.pre(
                {"style": {"width": "800px", "overflow": "scroll"}}, str(err)
            )
        else:
            if output.current is None:
                result = idom.html.pre("nothing to run")
            else:
                try:
                    result = output.current()
                except Exception as e:
                    result = e
                if not isinstance(result, idom.Component):
                    result = idom.html.pre(f"Expected component, not {result}")
        finally:
            idom.run = old_run
    else:
        result = idom.html.pre()

    return idom.html.div(
        idom.html.link(
            dict(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.63.1/codemirror.min.css",
                integrity="sha512-6sALqOPMrNSc+1p5xOhPwGIzs6kIlST+9oGWlI4Wwcbj1saaX9J3uzO3Vub016dmHV7hM+bMi/rfXLiF5DNIZg==",
                crossorigin="anonymous",
                referrerpolicy="no-referrer",
            )
        ),
        idom.html.style(".cm-editor { font-size: 0.85em; }"),
        Editor({"onChange": set_content}),
        idom.html.br(),
        result,
    )
