N = int(input())

num = 1

while num * num <= N:
    print(num * num)
    num += 1

n = int(input())

divider = 2

while n % divider != 0:
    divider += 1

print(divider)

N = int(input())

power_of_two = 1

while power_of_two <= N:
    print(power_of_two, end=" ")
    power_of_two *= 2

N = int(input())

power_of_two = 1

while power_of_two < N:
    power_of_two *= 2

if power_of_two == N:
    print("YES")
else:
    print("NO")

N = int(input())

k = 0

power_of_two = 1
while power_of_two < N:
    power_of_two *= 2
    k += 1

    print(k)



