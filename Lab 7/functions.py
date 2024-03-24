def min(a, b, c, d):
    min_val = a
    if b < min_val:
        min_val = b
    if c < min_val:
        min_val = c
    if d < min_val:
        min_val = d
    return min_val

a, b, c, d = map(int, input().split())

print(min(a, b, c, d))

def power(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

a, n = map(float, input().split())

print(power(a, int(n)))


def xor(x, y):
    if (x and not y) or (not x and y):
        return 1
    else:
        return 0

x, y = map(int, input().split())

print(xor(x, y))


