def quick_sort(values):
    if len(values) <= 1:
        return values[:]

    pivot = values[len(values) // 2]
    smaller = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    larger = [item for item in values if item > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)