a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(a, b + 1):
    if i % d == c:
        print(i, end=" ")


a = int(input())
b = int(input())

for i in range(a, b + 1):
    if (i ** 0.5).is_integer():
        print(i, end=" ")

x = int(input())
d = int(input())

x_str = str(x)

count = 0

for digit in x_str:
    if int(digit) == d:
        count += 1

print(count)

x = input()

sum_of_digits = 0

for digit in x:
    sum_of_digits += int(digit)

print(sum_of_digits)

x = input()

x_str = str(x)

for i in range(len(x_str) - 1, -1, -1):
    print(x_str[i], end="")

import math

x = int(input())

for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
        print(i)
        break

x = int(input())

for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=" ")

import math

x = int(input())

divisors_count = 0

for i in range(1, int(math.sqrt(x)) + 1):
    if x % i == 0:
        divisors_count += 2
        if i * i == x:
            divisors_count -= 1

print(divisors_count)

sum_of_numbers = 0

for _ in range(100):
    num = int(input())
    sum_of_numbers += num

print(sum_of_numbers)

N = int(input())

sum_of_numbers = 0

for _ in range(N):
    num = int(input())
    sum_of_numbers += num

print(sum_of_numbers)

binary_number = input()

decimal_number = 0

for i in range(len(binary_number) - 1, -1, -1):
    decimal_number += int(binary_number[i]) * (2 ** (len(binary_number) - 1 - i))

print(decimal_number)

N = int(input())

zero_count = 0

for _ in range(N):
    num = int(input())
    if num == 0:
        zero_count += 1

print(zero_count)














