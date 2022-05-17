# Created by Lucas Stoltman
# Program 5
# May 9th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import sort
import sys
import random
import timeit

# measure length 10, 50, 100, 200, 300, 400, 500, 1000
length = 100


# initialize list
arr = []
for i in range(length):
    arr.append(random.randint(0, length))


def print_time(time):
    # print("Time:", time, "seconds")
    print(time)


# --- bubble_sort() ---
print("\n---\033[1m", "bubble_sort()", "\033[0m---", )
random.shuffle(arr)
print(arr)
t = timeit.Timer(f"sort.bubble_sort({arr})", "import sort")
duration = t.timeit(1000)
print_time(duration)
sort.bubble_sort(arr)
print(arr)

# --- insertion_sort() ---
print("\n---\033[1m", "insertion_sort()", "\033[0m---", )
random.shuffle(arr)
print(arr)
t = timeit.Timer(f"sort.insertion_sort({arr})", "import sort")
duration = t.timeit(1000)
print_time(duration)
sort.insertion_sort(arr)
print(arr)

# --- merge_sort() ---
print("\n---\033[1m", "merge_sort()", "\033[0m---", )
random.shuffle(arr)
print(arr)
t = timeit.Timer(f"sort.merge_sort({arr})", "import sort")
duration = t.timeit(1000)
print_time(duration)
sort.merge_sort(arr)
print(arr)

# TODO implementation first
# --- iterative_merge_sort() ---
print("\n---\033[1m", "iterative_merge_sort()", "\033[0m---", )
random.shuffle(arr)
print(arr)
t = timeit.Timer(f"sort.iterative_merge_sort({arr})", "import sort")
duration = t.timeit(1000)
print_time(duration)
sort.iterative_merge_sort(arr)
print(arr)

# --- quick_sort() ---
print("\n---\033[1m", "quick_sort()", "\033[0m---", )
random.shuffle(arr)
print(arr)
t = timeit.Timer(f"sort.quick_sort({arr})", "import sort")
duration = t.timeit(1000)
print_time(duration)
sort.quick_sort(arr)
print(arr)

# --- shell_sort() ---
print("\n---\033[1m", "shell_sort()", "\033[0m---", )
random.shuffle(arr)
print(arr)
t = timeit.Timer(f"sort.insertion_sort({arr})", "import sort")
duration = t.timeit(1000)
print_time(duration)
sort.shell_sort(arr)
print(arr)
