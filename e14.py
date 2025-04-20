# Téo Sobrino Alves - 12557192 ex2, Lab de Alg. Avançados
# ex14

def solve(n, k):
    if k <= 1:
        return 1

    total = 0
    for i in range(n + 1):
        total = (total + solve(i, k - 1)) % 1000000

    return total

def main():
    MOD = 1000000
    MAX = 101

    tbl = [[0] * MAX for _ in range(MAX)]

    for i in range(MAX):
        tbl[i][0] = 0
        tbl[i][1] = 1

    for j in range(1, MAX):
        tbl[0][j] = 1

    for j in range(2, MAX):
        for i in range(1, MAX):
            tbl[i][j] = (tbl[i - 1][j] + tbl[i][j - 1]) % MOD

    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            break
        print(tbl[n][k])

if __name__ == "__main__":
    main()

