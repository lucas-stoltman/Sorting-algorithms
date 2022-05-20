# Created by Lucas Stoltman
# Program 5
# May 9th, 2022
# CSS 340 A,Dimpsey
# Version: 1.0

# Bubble Sort
def bubble_sort(arr: list):
    # run through the entire list n times
    for i in range(len(arr)):
        # run through the entire list once
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # swap values if they're out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return True


# Insertion Sort
def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        pointer = arr[i]
        j = i - 1
        while j >= 0 and pointer < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pointer
    return True


# Merge Sort (Recursive)
def merge_sort(arr: list):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k = k + 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j = j + 1
            k = k + 1


# Merge Sort (Iterative)
def iterative_merge_sort(arr: list):
    width = 1
    n = len(arr)

    while width < n:
        # start on the left
        left = 0
        while left < n:
            right = min(left + (width * 2 - 1), n - 1)
            mid = min(left + width - 1, n - 1)
            # combine left and right into a subarray
            merge(arr, left, mid, right)
            left += width * 2
        # double the subarray width after a merge
        width *= 2
    return arr


# iterative_merge_sort() helper function
def merge(arr: list, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[left + i]
    for i in range(0, n2):
        R[i] = arr[mid + i + 1]

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# Quick Sort
def quick_sort(arr: list):
    quick_sort_helper(arr, 0, len(arr) - 1)


# quick_sort() helper function
def quick_sort_helper(arr: list, first, last):
    if first < last:
        split_point = partition(arr, first, last)

        quick_sort_helper(arr, first, split_point - 1)
        quick_sort_helper(arr, split_point + 1, last)


# quick_sort() helper function
def partition(arr: list, first, last):
    pivot_value = arr[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and arr[left_mark] <= pivot_value:
            left_mark += 1
        while arr[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            temp = arr[left_mark]
            arr[left_mark] = arr[right_mark]
            arr[right_mark] = temp

    temp = arr[first]
    arr[first] = arr[right_mark]
    arr[right_mark] = temp
    return right_mark


# TODO Fix shell sort.
#  It shouldn't have the same runtime as insertion sort.
def shell_sort(arr: list):
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = arr[i]
            j = i
            while j >= gap and temp < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        if gap == 2:
            gap = 1
        else:
            gap = int(gap / 2.2)
