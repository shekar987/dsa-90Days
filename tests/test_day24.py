from problems.day24 import NumArray


def test_day24_examples():
    nums = NumArray([-2, 0, 3, -5, 2, -1])

    assert nums.sumRange(0, 2) == 1
    assert nums.sumRange(2, 5) == -1
    assert nums.sumRange(0, 5) == -3


def test_day24_handles_single_element_range():
    nums = NumArray([4, -1, 7])

    assert nums.sumRange(1, 1) == -1


def test_day24_handles_full_range():
    nums = NumArray([1, 2, 3, 4])

    assert nums.sumRange(0, 3) == 10


def test_day24_handles_negative_total():
    nums = NumArray([-3, -2, -1])

    assert nums.sumRange(0, 2) == -6
