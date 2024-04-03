if __name__ == '__main__':
    print("Hello, World!")

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    
    print(a / b)

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False



year = int(input())
print(is_leap(year))


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")


if __name__ == "__main__":
    n = int(input())
    scores = list(map(int, input().split()))
    

    unique_scores = list(set(scores))
    
   
    sorted_scores = sorted(unique_scores, reverse=True)
    
   
    print(sorted_scores[1])


if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])


    students.sort(key=lambda x: (x[1], x[0])) 

    second_lowest = students[0][1]
    for name, score in students:
        if score > second_lowest:
            second_lowest = score
            break

    for name, score in students:
        if score == second_lowest:
            print(name)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
   
    marks = student_marks[query_name]
    

    average_marks = sum(marks) / len(marks)
    
    print("{:.2f}".format(average_marks))

if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        if command[0] == 'insert':
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(lst)
        elif command[0] == 'remove':
            lst.remove(int(command[1]))
        elif command[0] == 'append':
            lst.append(int(command[1]))
        elif command[0] == 'sort':
            lst.sort()
        elif command[0] == 'pop':
            lst.pop()
        elif command[0] == 'reverse':
            lst.reverse()
