from typing import Tuple, Union

import numpy as np


def is_on_grid(x: float, nm: int = 1) -> bool:
    return np.isclose(snap_to_grid(x, nm=nm), x)


def assert_on_1nm_grid(x: float) -> None:
    assert np.isclose(snap_to_grid(x), x), f"{x} needs to be on 1nm grid"


def assert_on_2nm_grid(x: float) -> None:
    assert np.isclose(snap_to_2nm_grid(x), x), f"{x} needs to be on 1nm grid"


def snap_to_grid(x: Union[float, Tuple[float, float]], nm: int = 1) -> float:
    y = nm * np.round(np.array(x, dtype=float) * 1e3 / nm) / 1e3
    if isinstance(x, tuple):
        return tuple(y)
    elif type(x) in [int, float, str, float]:
        return float(y)
    return float(y)


def snap_to_2nm_grid(x: float) -> float:
    return snap_to_grid(x, nm=2)


def snap_to_5nm_grid(x: float) -> float:
    return snap_to_grid(x, nm=5)


def test_snap_to_grid():
    assert snap_to_grid(1.1e-3) == 0.001


def test_snap_to_2nm_grid():
    assert snap_to_2nm_grid(1.1e-3) == 0.002
    assert snap_to_2nm_grid(3.1e-3) == 0.004


def test_is_on_1nm_grid():
    assert not is_on_grid(0.1e-3)
    assert is_on_grid(1e-3)


def test_is_on_2nm_grid():
    assert not is_on_grid(1.1e-3, 2)
    assert not is_on_grid(1e-3, 2)
    assert is_on_grid(2e-3, 2)


if __name__ == "__main__":
    test_is_on_2nm_grid()
    # print(snap_to_grid(1.1e-3))
    # print(snap_to_2nm_grid(1.1e-3))
    # print(snap_to_2nm_grid(3.1e-3))

    # print(on_1nm_grid(1.1e-3))
    # print(on_1nm_grid(1e-3))

    # print(on_2nm_grid(1.1e-3))
    # print(on_2nm_grid(1e-3))
    # print(on_2nm_grid(2e-3))
