import math


a = int(input())
b = int(input())

c = math.sqrt(a**2 + b**2)

print(c)


number = int(input())

next_number = number + 1
prev_number = number - 1

print("The next number for the number", number, "is", next_number, end=".\n")
print("The previous number for the number", number, "is", prev_number, end=".")

N = int(input())
K = int(input())

apples_per_student = K // N

print(apples_per_student)

N = int(input())
K = int(input())

apples_left = K % N

print(apples_left)

v = int(input())
t = int(input())

distance = v * t

if v > 0:
    final_position = (distance % 109)
else:
    final_position = (109 + (distance % 109)) % 109

print(final_position)



