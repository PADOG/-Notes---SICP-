# Exercise 1.5:
# Ben Bitdiddle has invented a test to determine whether the interpreter he is faced with is using applicative-order evaluation or normal-order evaluation. He defines the following two procedures:

# lisp

# (define (p) (p))
# (define (test x y)
#         (if (= x 0) 0 y))

# python

def p():
    p()

def test(x, y):
    if x == 0:
        return 0
    else:
        return y

# Then he evaluates the expression

# lisp

# (test 0 (p))

# python

# test(0, p())

# What behavior will Ben observe with an interpreter that uses applicative-order evaluation? 
# What behavior will he observe with an interpreter that uses normal-order evaluation?
# Explain your answer.
# (Assume that the evaluation rule for the special form if is the same whether the interpreter is using normal or applicative order: The predicate expression is evaluated first, and the result determines whether to evaluate the consequent or the alternative expression.)

# applicative-order evaluation
# 编译器先计算参数，之后将参数带入函数
# normal-order evaluation
# 编译器先完全展开函数，之后对完全展开式进行计算

# python/lisp 使用 applicative-order evaluation
# test(0, p()) 会先技术算参数 0 与 p() 
# 其中 p() 为递归函数，导致 RecursionError: maximum recursion depth exceeded 错误：超过最大递归深度

# 若使用 normal-order evalution
# test(0, p()) 会先展开函数:

# x = 0
# if x == 0:
#     return 0
# else:
#     return p()

# 展开后按顺序执行，得到返回值 0 
