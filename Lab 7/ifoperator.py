a = int(input())
b = int(input())

if a > b:
    print(a)
else:
    print(b)

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")

test_system_answer = int(input())
student_answer = int(input())

if student_answer == 1:
    if test_system_answer == 1:
        print("YES")
    else:
        print("NO")
else:
    if test_system_answer != 1:
        print("YES")
    else:
        print("NO")


x = int(input())

if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)


num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(1)
elif num1 < num2:
    print(2)
else:
    print(0)





