def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)  # Before pi
        quick_sort(arr, pi + 1, high)  # After pi


def partition(arr, low, high):
    pivot = arr[high]  # pivot
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Example usage:
arr = [10, 80, 30, 90, 40, 50, 70]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [10, 30, 40, 50, 70, 80, 90]
