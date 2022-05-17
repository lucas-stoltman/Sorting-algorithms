# Created by Lucas Stoltman
# Program 5
# May 9th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import sort
import sys
import random

# default values
sort_type = "bubble"
length = 10
display = False

# no arguments
if len(sys.argv) == 1:
    print("No arguments entered.")

# sort type
if len(sys.argv) > 1:
    try:
        if sys.argv[1] == "bubble" or "insertion" or "merge" or "imerge" or "quick" or "shell":
            sort_type = str(sys.argv[1])
        else:
            print("Sort not recognized.")
            print("Please enter one of the following words as the first argument:")
            print("\nbubble\ninsertion\nmerge\nimerge\nquick\nshell\n")
            print("Example of valid input:\nsorter.py bubble 25 PRINT\n")

    except ValueError:
        print("Please enter a string.")
        print("You entered:", sys.argv[1], "\n")

# list length
if len(sys.argv) >= 3:
    try:
        if int(sys.argv[2]) > 0:
            length = int(sys.argv[2])
        else:
            print("Please enter a positive integer.")
            print("Default value (10) used.\n")

    except ValueError:
        print("Please enter a whole number as the second argument.")
        print("You entered:", sys.argv[2], "\n")

# PRINT (optional)
if len(sys.argv) == 4:
    try:
        if sys.argv[3] == "PRINT":
            display = True
        else:
            print("You entered:", sys.argv[3], "\n")
            print("Did you mean \"PRINT\"?")

    except ValueError:
        print("Error with third argument")
        print("You entered:", sys.argv[3], "\n")


# Initialize a random list
arr = []
for i in range(length):
    arr.append(random.randint(0, length))


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
    else:
        print("Not sorted!")


# sorting with PRINT argument
if display:
    print("Before\t", arr)
    sort(sort_type)
    print("After\t", arr)
# sorting without PRINT argument
else:
    sort(sort_type)
