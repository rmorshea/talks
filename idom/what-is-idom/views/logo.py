@idom.element
async def main(self, index=0):
    with open("static/logo.png", "rb") as f:
        image = idom.Image("png")
        image.io.write(f.read())
        image_model = await image.render()
        image_model["attributes"]["style"] = {"transform": "translate(0px,-200px)"}
        return idom.html.div(
            image_model,
            style={
                "margin-top": "30px",
                "margin-bottom": "30px",
                "height": "400px",
                "overflow": "hidden",
                "position": "relative",
            }
        )
