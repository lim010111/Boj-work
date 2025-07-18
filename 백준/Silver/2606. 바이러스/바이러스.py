def count_virus(n: int, connection: list[list], infected: list[bool]) -> int:

    def dfs(start):
        infected[start] = True

        for connected in connection[start]:
            if not infected[connected]:
                dfs(connected)

    dfs(1)

    return infected.count(True) - 1


if __name__ == "__main__":
    n = int(input())

    connection = [[] for _ in range(n + 1)]
    for _ in range(int(input())):
        c1, c2 = map(int, input().split())
        connection[c1].append(c2)
        connection[c2].append(c1)

    infected = [False] * (n + 1)

    print(count_virus(n, connection, infected))