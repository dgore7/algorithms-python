from collections import deque


def bfs(cap, num):
    q = deque()
    q.append(num)
    while len(q) is not 0:
        num = q.popleft()
        if num <= cap:
            print(num, end=" ")
            last_dig = num % 10

            if last_dig == 0:
                q.append( num * 10 + last_dig + 1)

            elif last_dig == 9:
                q.append(num * 10 + last_dig - 1)

            else:
                q.append(num * 10 + last_dig - 1)
                q.append(num * 10 + last_dig + 1)


def print_jumping_numbers(num):
    print(0, end=" ")
    for i in range(1,10):
        bfs(num, i)


print_jumping_numbers(4000)