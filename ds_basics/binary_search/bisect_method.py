import bisect



# This sorted list will be used throughout this lesson
# to showcase the functionality of the "bisect" method.
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# -10 is at index 1
print(bisect.bisect_left(A, -10))

# First occurrence of 285 is at index 6
print(bisect.bisect_left(A, 285))


# Index position to right of -10 is 2.
print(bisect.bisect_right(A, -10)) 

# Index position after last occurrence of 285 is 9.
print(bisect.bisect_right(A, 285))


# Index position to right of -10 is 2. (Same as bisect_right)
print(bisect.bisect(A, -10)) 

# Index position after last occurrence of 285 is 9. (Same as bisect_right).
print(bisect.bisect(A, 285))


print(A)
bisect.insort_left(A, 108)
print(A)

bisect.insort_right(A, 108)
print(A)