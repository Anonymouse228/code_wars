import pytest

from smaller_than_me_2 import smaller


smaller_data_set = (
    ([5, 4, 3, 2, 1], [4, 3, 2, 1, 0]),
    ([1, 2, 3], [0, 0, 0]),
    ([1, 2, 0], [1, 1, 0]),
    ([1, 2, 1], [0, 1, 0]),
    ([1, 1, -1, 0, 0], [3, 3, 0, 0, 0]),
    ([5, 4, 7, 9, 2, 4, 4, 5, 6], [4, 1, 5, 5, 0, 0, 0, 0, 0]),
    ([5, 4, 7, 9, 2, 4, 1, 4, 5, 6], [5, 2, 6, 6, 1, 1, 0, 0, 0, 0]),
)


@pytest.mark.parametrize('array, expected_array', smaller_data_set)
def test_smaller_equals(array, expected_array):
    assert smaller(array) == expected_array
