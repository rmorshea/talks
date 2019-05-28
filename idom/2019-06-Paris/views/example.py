@idom.element
async def main(self, index=0):
    events = idom.Events()

    @events.on("click")
    async def change():
        self.update(index + 1)

    url = f"https://picsum.photos/800/300?image={index}"
    return idom.node("img", src=url, eventHandlers=events, width="100%")
