from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
poke_dict = {input().rstrip(): i for i in range(1, n + 1)}
problems = [input().rstrip() for _ in range(m)]

poke_names = [''] + list(poke_dict.keys())
answers = []
for problem in problems:
    if problem.isdigit():
        answers.append(poke_names[int(problem)])
    else:
        answers.append(poke_dict[problem])

print(*answers, sep='\n')