# Created by Lucas Stoltman
# Program 5
# May 9th, 2022
# CSS 340 A,Dimpsey
# Version: 1.0

# Bubble Sort
def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return True


# TODO Insertion Sort
def insertion_sort(arr: list):
    for i in range(len(arr)):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
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
