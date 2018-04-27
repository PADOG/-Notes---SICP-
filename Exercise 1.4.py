# Exercise 1.4:
# Observe that our model of evaluation allow for combinations
# whose operators are compound expressions.Use this observation 
# to describe the behavior of the following procedure:

# lisp

# (define (a-plus-abs-b a b)
#         ((if (> b 0) + -) a b))

# python

def APlusAbsB(a, b):
    if b > 0:
        return a + b
    else:
        return a - b

print('APlusAbsB(1, 2) = ' + str(APlusAbsB(1, 2)) + '\n')
print('AplusAbsB(1,-2) = ' + str(APlusAbsB(1,-2)) + '\n')
