# Téo Sobrino Alves - 12557192 ex2, Lab de Alg. Avançados
# ex10

def is_valid(T, i, j):
    for k in range(8):
        if k == i:
            continue
        if T[k] == -1:
            continue
        if T[k] == j:
            return False
        if abs(i - k) == abs(j - T[k]):
            return False
    return True

def solve(T, i, sols):
    if i == 8:
        sols.append(T[:])
        return
    
    if T[i] != -1:
        solve(T, i + 1, sols)
        return
    
    for j in range(8):
        if is_valid(T, i, j):
            T[i] = j
            solve(T, i + 1, sols)
            T[i] = -1

def main():
    n = int(input())
    
    for _ in range(n):
        T = [-1] * 8
        sols = []
        
        i, j = map(int, input().split())
        T[j - 1] = i - 1
        
        solve(T, 0, sols)
        sols.sort()
        
        for idx, sol in enumerate(sols, 1):
            print(idx, *[v + 1 for v in sol])
        print()

if __name__ == "__main__":
    main()
