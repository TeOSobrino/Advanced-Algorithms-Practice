
# Téo Sobrino Alves - 12557192 ex2, Lab de Alg. Avançados
# ex12

def solve(cuts, a, b, memo):
    if b <= a:
        return 0

    if (a, b) in memo:
        return memo[(a, b)]

    cost = b - a
    tentative_cost = float('inf')
    updated_cost = False

    for cut in cuts:
        if a < cut < b:
            maybe_cost = solve(cuts, cut, b, memo) + solve(cuts, a, cut, memo)
            tentative_cost = min(tentative_cost, maybe_cost)
            updated_cost = True

    if not updated_cost:
        memo[(a, b)] = 0
        return 0

    cost += tentative_cost
    memo[(a, b)] = cost

    return cost

def main():
    while True:
        l = int(input())
        if l == 0:
            break

        n = int(input())
        cuts = list(map(int, input().split()))
        memo = {}
        print(f"O custo mínimo de separação é {solve(cuts, 0, l, memo)}.")

if __name__ == "__main__":
    main()