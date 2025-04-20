# Téo Sobrino Alves - 12557192 ex2, Lab de Alg. Avançados
# ex11

def main():
    n = int(input())

    for _ in range(n):
        m, c = map(int, input().split())

        tbl = [[0 for _ in range(m)] for _ in range(c)]

        for a in range(c):
            k, *rest = map(int, input().split())
            if len(rest) < k:
                rest += list(map(int, input().split()))
            items = rest[:k]

            if a == 0:
                for item in items:
                    remaining = m - item
                    if remaining >= 0:
                        tbl[a][remaining] = 1
            else:
                for b in range(m):
                    if tbl[a - 1][b] == 1:
                        for item in items:
                            remaining = b - item
                            if remaining >= 0:
                                tbl[a][remaining] = 1

        min_val = -1
        for b in range(m):
            if tbl[c - 1][b] == 1:
                min_val = b
                break

        if min_val > -1:
            print(m - min_val)
        else:
            print("no solution")

if __name__ == "__main__":
    main()