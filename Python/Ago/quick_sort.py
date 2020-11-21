def quick_sort(array):

    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        left = [i for i in array[1:] if i <= pivot]
        right = [i for i in array[1:] if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([10, 20, 11, 3, 2, 2, 5]))
