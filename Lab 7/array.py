N = int(input())

array = list(map(int, input().split()))

for i in range(0, N, 2):
    print(array[i], end=" ")

N = int(input())

array = list(map(int, input().split()))

for num in array:
    if num % 2 == 0:
        print(num, end=" ")


N = int(input())

array = list(map(int, input().split()))

positive_count = 0

for num in array:
    if num > 0:
        positive_count += 1

print(positive_count)

N = int(input())

array = list(map(int, input().split()))

count = 0

for i in range(1, N):
    if array[i] > array[i - 1]:
        count += 1

print(count)

N = int(input())

array = list(map(int, input().split()))

result = "NO"

for i in range(N - 1):
    if array[i] * array[i + 1] > 0:
        result = "YES"
        break

print(result)

N = int(input())

array = list(map(int, input().split()))

count = 0

for i in range(1, N - 1):
    if array[i] > array[i - 1] and array[i] > array[i + 1]:
        count += 1

print(count)

N = int(input())

array = list(map(int, input().split()))

for i in range(N // 2):
    array[i], array[N - i - 1] = array[N - i - 1], array[i]

print(*array)








