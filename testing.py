# Created by Lucas Stoltman
# Program 5
# May 9th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import sort
import sys

# sort_type = str(sys.argv[1])
# length = eval(sys.argv[2])

# PRINT (optional)
# display = str(sys.argv[3])

# Driver


# --- bubble_sort() ---
print("\n---\033[1m", "bubble_sort()", "\033[0m---", )
bubble_list = [5, 2, 5, 6, 3, 9, 2, 1]
print(bubble_list)
sort.bubble_sort(bubble_list)
print(bubble_list)


# --- insertion_sort() ---
print("\n---\033[1m", "insertion_sort()", "\033[0m---", )
insertion_list = [5, 2, 5, 6, 3, 9, 2, 1]
print(insertion_list)
sort.insertion_sort(insertion_list)
print(insertion_list)


# --- merge_sort() ---
print("\n---\033[1m", "merge_sort()", "\033[0m---", )
merge_list = [5, 2, 5, 6, 3, 9, 2, 1]
print(merge_list)
sort.merge_sort(merge_list)
print(merge_list)

