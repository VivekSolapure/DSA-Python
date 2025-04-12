from sys import stdin, stdout
from collections import defaultdict

def dfs(u, p):
    global A, B, a, adj, c
    for v in adj[u]:
        if v == p:
            continue
        dfs(v, u)

    A[u] = a[u]
    B[u] = 0

    for v in adj[u]:
        if v == p:
            continue
        if A[v] <= B[v]:
            B[u] += B[v]
            A[u] += B[v]
        else:
            B[u] += A[v]
            x = A[v] - B[v]
            if x <= 2 * c:
                A[u] += B[v]
            else:
                A[u] += A[v] - 2 * c

num_tests = int(stdin.readline().strip())

for _ in range(num_tests):
    n, c = map(int, stdin.readline().strip().split())

    a = [0] * (n + 1)
    adj = defaultdict(list)
    A = [0] * (n + 1)
    B = [0] * (n + 1)

    for i in range(1, n + 1):
        a[i] = int(stdin.readline().strip())

    for _ in range(n - 1):
        u, v = map(int, stdin.readline().strip().split())
        adj[u].append(v)
        adj[v].append(u)

    dfs(1, 0)
    stdout.write(f"{max(A[1], B[1])}\n")

