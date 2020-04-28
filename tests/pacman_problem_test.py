from pytest import raises
from pac_man.pacman_problem import PacManProblem


def test_pacman_initializes():
    pb = PacManProblem((0, 0), (0, 1), [["S", "F", 3, 4], [1, 2, 3, 4]])

    assert pb