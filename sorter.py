# Created by Lucas Stoltman
# Program 5
# May 9th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import sort
import sys
import random

# default values
sort_type = ""
length = 10
display = False

# TODO validate string input
# sort type
if len(sys.argv) >= 2:
    sort_type = str(sys.argv[1])

# TODO validate numeric input
# list length
if len(sys.argv) >= 3:
    length = eval(sys.argv[2])

# PRINT (optional)
if len(sys.argv) == 4:
    if sys.argv[3] == "PRINT":
        display = True

# Initialize a random list
arr = []
for i in range(length):
    arr.append(random.randint(0, 100))


def sort(s_type: ""):
    import sort
    global arr
    if sort_type == "bubble":
        return sort.bubble_sort(arr)
    elif sort_type == "insertion":
        return sort.insertion_sort(arr)
    elif sort_type == "merge":
        return sort.merge_sort(arr)
    elif sort_type == "imerge":
        return sort.iterative_merge_sort(arr)
    elif sort_type == "quick":
        return sort.quick_sort(arr)
    elif sort_type == "shell":
        return sort.shell_sort(arr)


if display:
    print("Before\t", arr)
    sort(sort_type)
    print("After\t", arr)
else:
    sort(sort_type)
