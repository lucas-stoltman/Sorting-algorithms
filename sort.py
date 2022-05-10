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
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                # swap values if they're out of order
                arr[j], arr[j+1] = arr[j+1], arr[j]
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


# TODO Merge Sort
# def marge_sort():

# TODO Non-Recursive, one extra list Merge Sort (We’ll call this improved version,
# IterativeMergeSort from here on out in this homework)
# def iterative_merge_sort():

# TODO Quick Sort
# def quick_sort():

# TODO Shell Sort
# def shell_sort():
