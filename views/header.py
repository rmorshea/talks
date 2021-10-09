import idom


def main():
    return idom.html.div(
        idom.html.link(
            {
                "rel": "stylesheet",
                "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css",
                "crossorigin": "anonymous",
            }
        ),
        idom.html.style(
            """
            button {
                display: inline-block;
                border: none;
                padding: 0.7rem 1rem;
                margin: 4px;
                text-decoration: none;
                background: #0069ed;
                color: #ffffff;
                font-family: sans-serif;
                font-size: 1rem;
                cursor: pointer;
                text-align: center;
                transition: background 250ms ease-in-out,
                            transform 150ms ease;
                -webkit-appearance: none;
                -moz-appearance: none;
            }
            button:hover,
            button:focus {
                background: #0053ba;
            }

            button:focus {
                outline: 1px solid #fff;
                outline-offset: -4px;
            }

            button:active {
                transform: scale(0.99);
            }
            """
        ),
    )
