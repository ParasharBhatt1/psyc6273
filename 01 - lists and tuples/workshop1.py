# workshop1.py Lecture 1 workshop problems

# Add code below the following comments, to solve the stated problems.

# 1. Create a list x that contains the numbers 1 to 10.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2. Set a variable y equal to the following sublists of x. Where possible,
# write your code so that it works for any length of x, e.g., it still
# works if x has 20 elements rather than 10.
y=x
# 2a. the first element of x
x[0]
# 2b. the first five elements of x
x[0:5]
# 2c. the last element of x
x[-1]
# 2d. the last five elements of x
x[-5:]
# 2e. every second element of x, starting with the first element
x[0::2]
# 2f. every third element of x, starting with the second element
x[1::3]
# 2g. all the elements of x, in reverse order
x[::-1]
# 2h. every second element of x, counting back from the last element
x[::-2]
# 2i. the first three elements of x and the last three elements of x
x[0:3] + x[-3:]
# 2j. the first five elements of x, repeated ten times, i.e., the list
#    [ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ... ], with ten repetitions
(x[0:5]) * 10
# 2k. the largest element of x, repeated five times
[max(x)] * 5
# 2l. the smallest element of x, repeated a number of times equal to
#     the largest element of x
[(minx(x))] * max(x)
# 3. Change the list x as follows.

# 3a. set the first element to zero
x[0] = 0
# 3b. set the last three elements to zero

# 3c. set every third element, starting with the first, to equal the
#     largest element of x

# 3d. delete the fourth and fifth elements of x

# 3e. delete the first occurrence of the largest element of x

# 3f. delete the last element of x

# 3g. append the value 11 to the end of x

# 3h. append the first three elements of x to the end of x

# 3i. sort the elements of x

# 4. Make y equal to the list x, in such a way that if you change an 
#    element of x, the corresponding element of y changes as well.

# 5. Make y equal to the list x, in such a way that if you change an
#    element of x, the corresponding element of y does not change.

# 6. Create a tuple z that contains the following elements.

# 6a. the number 50

# 6b. the number 50, repeated three times

# 6c. the numbers 1, 2, and 3, in that order, repeated five times

