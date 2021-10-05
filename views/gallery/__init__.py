import idom

from .matplotlib_plot import PolynomialPlot
from .pigeon_maps import MapWithMarkers
from .simple_dashboard import RandomWalk
from .audio_player import PlayDinosaurSound
from .snake_game import GameView


def line_break():
    return idom.html.hr({"style": {"margin": "70px 0"}})


def main():
    return idom.html.div(
        RandomWalk(),
        line_break(),
        PlayDinosaurSound(),
        line_break(),
        GameView(),
        line_break(),
        MapWithMarkers(),
        line_break(),
        PolynomialPlot(),
    )
