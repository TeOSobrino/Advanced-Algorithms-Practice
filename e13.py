# Téo Sobrino Alves - 12557192 ex2, Lab de Alg. Avançados
# ex13

def solve(i, costs, mask, n, tbl):
    if mask == (1 << n) - 1:
        return costs[i][0]

    if tbl[i][mask] != -1:
        return tbl[i][mask]

    min_cost = float('inf')
    for k in range(n):
        if not (mask & (1 << k)):
            new_mask = mask | (1 << k)
            min_cost = min(min_cost, costs[i][k] + solve(k, costs, new_mask, n, tbl))

    tbl[i][mask] = min_cost
    return min_cost

def manh_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main():
    n = int(input())

    for _ in range(n):
        w, h = map(int, input().split())
        ox, oy = map(int, input().split())
        m = int(input())
        
        points = [(ox, oy)]

        for _ in range(m):
            px, py = map(int, input().split())
            points.append((px, py))

        num_points = m + 1
        costs = [[0] * num_points for _ in range(num_points)]

        for i in range(num_points):
            for j in range(num_points):
                costs[i][j] = manh_dist(points[i], points[j])

        tbl = [[-1] * (1 << num_points) for _ in range(num_points)]

        print(f"A menor rota tem tamanho {solve(0, costs, 1, num_points, tbl)}.")

if __name__ == "__main__":
    main()
