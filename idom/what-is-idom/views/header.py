import idom


def Main():
    return idom.html.link(
        {
            "rel": "stylesheet",
            "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css",
            "crossorigin": "anonymous",
        }
    )
