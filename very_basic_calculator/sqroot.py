def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


def bin_coef(m, k):  # m choose k
    numerator = 1
    for factor in range(0, k):
        numerator = numerator * (m - factor)
    denominator = fact(k)
    coef = numerator / denominator
    return coef


def sqroot(num):
    exp = len(str(num))
    x = (num / (10**exp)) - 1
    sum = 0
    for term in range(10):
        sum += bin_coef(1 / 2, term) * (x**term)
    if exp % 2 == 0:
        result = sum * (10 ** (exp / 2))
    else:
        result = sum * 3.16227766017 * (10 ** ((exp - 1) / 2))
    return result
