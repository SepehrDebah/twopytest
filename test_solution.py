from solution import quick_sort

def test_quick_sort_unsorted_numbers():
    assert quick_sort([7, 2, 5, 1, 9, 2]) == [1, 2, 2, 5, 7, 9]

def test_quick_sort_handles_empty_and_sorted_input():
    assert quick_sort([]) == []
    assert quick_sort([1, 2, 3]) == [1, 2, 3]