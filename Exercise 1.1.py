# Exercise 1.1:
# Below is a sequence of experessions.What is the result 
# printed by the interpreter in response to each expression?
# Assume that the sequence is to be evaluated in the order in
# which it is presented.

# lisp

# 10
print(10)

# (+ 5 3 4)
print(5 + 3 + 4)

# (- 9 1)
print(9 - 1)

# (/ 6 2)
print(6/2)

# (+ (* 2 4) (- 4 6))
print((2 * 4) + (4 - 6))

# (define a 3)
a = 3
print(a)

# (define b (+ a 1))
b = a + 1
print(b)

# (+ a b (* a b))
print(a + b + (a * b))

# (= a b)
print(a == b)

# (if (and (> b a) (< b (* a b)))
#   b
#   a)
if (b > a) & (b < (a * b)):
    print(b)
else:
    print(a)

# (cond ((= a 4) 6)
#       ((= b 4) (+ 6 7 a))
#       (else 25))
def num0(a,b):
    if a == 4:
        return 6
    elif b == 4:
        return 6 + 7 + a
    else:
        return 25
print(num0(a,b))

# (+ 2 (if (> b a) b a))
def num1(a,b):
    if b > a:
        return b
    else:
        return a
print(2 + num1(a,b))

# (* (cond ((> a b) a)
#          ((< a b) b)
#          (else -1))
#    (+ a 1))
def num2(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return -1
print(num2(a,b) * (a + 1))
