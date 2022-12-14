"""Module with game constants."""
from dataclasses import dataclass


@dataclass
class Sign:
    """Class for sign mark and value."""
    sign: str
    value: int


class SignObjects:
    """Class contains all possible sings for game."""
    empty_sign = Sign(sign=" ", value=0)
    ship_sign = Sign(sign="0", value=10)
    miss_sign = Sign(sign="*", value=100)
    hit_sign = Sign(sign="X", value=1000)


AREA_AROUND = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


SHIPS_COORDINATES = (
    [(10, 1), (10, 2), (10, 3), (10, 4)],
    [(10, 6), (10, 7), (10, 8)],
    [(8, 1), (8, 2), (8, 3)],
    [(1, 2), (2, 2)],
    [(8, 5), (8, 6)],
    [(8, 8), (8, 9)],
    [(6, 1)],
    [(6, 3)],
    [(6, 5)],
    [(6, 7)]
)
