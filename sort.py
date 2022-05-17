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


def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k = k + 1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1


# TODO Non-Recursive, one extra list Merge Sort
# TODO Change comments
# def iterative_merge_sort(a_list):


# TODO Sedgewick points
# TODO Quick Sort
# TODO Quick Sort Helper (arr, low, high)
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)


def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)


def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark += 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp

    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark


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
