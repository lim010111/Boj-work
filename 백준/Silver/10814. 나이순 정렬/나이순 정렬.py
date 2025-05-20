from sys import stdin

input = stdin.readline

n = int(input())
users = sorted([tuple(input().split()) for _ in range(n)],
               key=lambda user: int(user[0]))

[print(*user) for user in users]