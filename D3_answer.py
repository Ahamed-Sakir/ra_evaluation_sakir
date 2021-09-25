def fin(n):
    a, b = 0, 1
    for i in range(1, n + 1):
        if i == 1:
            yield a
            a, b = 1, 2
        else:
            yield a
            a, b = b, a + b


lst = list(map(int, input().split(",")))
for x in range(len(lst)):
    fib = list(fin(lst[x]))
    print(*fib, sep=", ")
