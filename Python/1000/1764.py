N, M = map(int, input().split())
A = set(list(input() for _ in range(N)))
B = set(list(input() for _ in range(M)))
AB = sorted(list(A & B))
print(len(AB))
print(*AB, sep="\n")
