from our_library.some_functions import add_10
import pytest
import numpy as np


def test_add_10():
    assert add_10(2) == 12
    assert add_10(-1) == 9
    assert add_10(0) == 10


SEEDS = [0, 1, 2, 123, 456]


@pytest.mark.parametrize("seed", SEEDS, ids=[f"{s}" for s in SEEDS])
def test_add_10_against_numpy(seed):
    """Test our function against numpy."""

    # Sample two random vectors, add them
    np.random.seed(seed)
    numbers = np.random.rand(20)
    np_add_10 = numbers + 10

    # Test against our function
    our_add_10 = np.array([add_10(a) for a in numbers])
    np.testing.assert_array_equal(np_add_10, our_add_10)
