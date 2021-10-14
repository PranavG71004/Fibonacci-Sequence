# def multiply(x, y):
#     result = x * y
#     result_1 = int(result)
#     return result_1
#
# forty_two = multiply(10.5, 4)
# print(forty_two)
#
# for value in range(1, 11):
#     table_1 = multiply(98, value)
#     print(table_1)

def fibonacci(n: int) -> int:
    """Return the `n`th Fibonacci number, for positive `n`."""

    if 0<= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))
