import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers returns a streak of 0."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test a simple case with one streak."""
    assert longest_positive_streak([1, 2, 0, 4, 5]) == 2

def test_multiple_streaks_longest_first():
    """Test with multiple streaks where the longest is first."""
    assert longest_positive_streak([1, 2, 3, 0, 4, 5]) == 3

def test_multiple_streaks_longest_last():
    """Test with multiple streaks where the longest is last."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 7]) == 4

def test_streaks_with_negatives_and_zeros():
    """Test streaks separated by negative numbers and zeros."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_streak_of_ones():
    """Test a streak composed of only ones."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_single_element_list_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_list_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0