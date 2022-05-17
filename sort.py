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
# def iterative_merge_sort(arr: list):
# width = 1
# n = len(arr)
# # subarray size grows by powers of 2
# # since growth of loop condition is exponential,
# # time consumed is logarithmic (log2n)
# while width < n:
#     # always start from leftmost
#     left = 0
#     while left < n:
#         r = min(left + (width * 2 - 1), n - 1)
#         m = min(left + width - 1, n - 1)
#         # final merge should consider
#         # unmerged sublist if input arr
#         # size is not power of 2
#         merge(arr, left, m, r)
#         left += width * 2
#     # Increasing sub array size by powers of 2
#     width *= 2
# return arr

# Bottom-up merge sort is a non-recursive variant of the merge sort,
# in which the array is sorted by a sequence of passes.
# During each pass, the array is divided into blocks of size m.
# (Initially, m = 1). Every two adjacent blocks are merged (as in normal merge sort),
# and the next pass is made with a twice larger value of m.


# def partition(arr, low, high):
#     i = (low - 1)  # index of smaller element
#     pivot = arr[high]  # pivot
#
#     for j in range(low, high):
#
#         # If current element is smaller than or
#         # equal to pivot
#         if arr[j] <= pivot:
#             # increment index of smaller element
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1


# TODO Sedgewick points
# TODO Quick Sort
# TODO Quick Sort Helper (arr, low, high)
# def quick_sort(arr: list):
#     if len(arr) == 1:
#         return arr
#     if low < high:
#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr, low, high)
#
#         # Separately sort elements before
#         # partition and after partition
#         quick_sort(arr, low, pi - 1)
#         quick_sort(arr, pi + 1, high)


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
