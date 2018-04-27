# Exercise 1.3:
# Define a procedure that takes three numbers as arguments and
# returns the sum of the squares of the two larger numbers.

# lisp

# (define (MaxTwoSum a b c)
#         (cond ((and (< a b) (< a c)) (+ b c))
#               ((and (< b a) (< b c)) (+ a c))
#               ((and (< c a) (< c b)) (+ a b))))

# python

def MaxTwoSum(a, b, c):
    if (a <= b) & (a <= c):
        return b + c
    if (b <= a) & (b <= c):
        return a + c
    if (c <= a) & (c <= b):
        return a + b

print('MaxTwoSum(1,2,3) = ' + str(MaxTwoSum(1,2,3)))
