#działa
def staircase(n):
    if 0 < n < 100:
        for i in range(n):
            print((n - i - 1) * ' ', end='')
            print((i + 1) * '#')


n = 6
staircase(n)
