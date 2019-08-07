@idom.element
async def main(self, index=10):
    events = idom.Events()

    @events.on("click")
    async def change(event):
        self.update(index + 1)

    style = {"border": "7px solid"}
    url = f"https://picsum.photos/800/500?image={index}"
    return idom.node("img", src=url, style=style, eventHandlers=events, width="100%")
