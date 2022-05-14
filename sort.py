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


# Merge Sort
def merge_sort(arr: list):
    if len(arr) > 1:
        mid = len(arr) // 2

        # LEFT half
        left = arr[mid:]
        # RIGHT half
        right = arr[:mid]

        # recursive calls
        merge_sort(left)
        merge_sort(right)

        # reset loop variables
        i = j = k = 0

        # ordering values within arr[]
        while i < len(left) and j < len(right):
            # if comparison is already sorted
            if left[i] < right[j]:
                # place LEFT value to the left
                arr[k] = left[i]
                i += 1
            else:
                # place RIGHT value to the left
                arr[k] = right[j]
                j += 1
            k += 1

        # checking extra elements after the mergesort
        # LEFT side
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        # RIGHT side
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1


# TODO Non-Recursive, one extra list Merge Sort (We’ll call this improved version,
# IterativeMergeSort from here on out in this homework)
# def iterative_merge_sort():



# TODO Sedgewick points
# TODO Quick Sort
# def quick_sort(arr: list):



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