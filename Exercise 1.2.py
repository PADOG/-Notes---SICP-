# Exercise 1.2:
# Translate the following expression into prefix from:
# (5 + 4 + (2 - (3 - (6 + 4/5)))) / (3 * (6 -2) * (2 - 7))

# lisp

# (/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5))))) (* 3 (- 6 2) (- 2 7)))

# python

Num =  (5 + 4 + (2 - (3 - (6 + 4/5)))) / (3 * (6 -2) * (2 - 7))
print(Num)
