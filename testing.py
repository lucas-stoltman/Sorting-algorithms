# Created by Lucas Stoltman
# Program 5
# May 9th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import sort
import sys
import random

length = 10

# initialize list
arr = []
for i in range(length):
    arr.append(random.randint(0, 10))


# --- bubble_sort() ---
print("\n---\033[1m", "bubble_sort()", "\033[0m---", )
random.shuffle(arr)
print(arr)
sort.bubble_sort(arr)
print(arr)


# --- insertion_sort() ---
print("\n---\033[1m", "insertion_sort()", "\033[0m---", )
random.shuffle(arr)
print(arr)
sort.insertion_sort(arr)
print(arr)


# --- merge_sort() ---
print("\n---\033[1m", "merge_sort()", "\033[0m---", )
random.shuffle(arr)
print(arr)
sort.merge_sort(arr)
print(arr)


# TODO implementation first
# # --- iterative_merge_sort() ---
# print("\n---\033[1m", "iterative_merge_sort()", "\033[0m---", )
# random.shuffle(arr)
# print(arr)
# sort.iterative_merge_sort(arr)
# print(arr)


# TODO implementation first
# # --- quick_sort() ---
# print("\n---\033[1m", "quick_sort()", "\033[0m---", )
# random.shuffle(arr)
# print(arr)
# sort.quick_sort(arr)
# print(arr)


# --- shell_sort() ---
print("\n---\033[1m", "shell_sort()", "\033[0m---", )
random.shuffle(arr)
print(arr)
sort.shell_sort(arr)
print(arr)
