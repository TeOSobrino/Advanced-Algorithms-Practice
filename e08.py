# Téo Sobrino Alves - 12557192 ex2, Lab de Alg. Avançados
# ex8

from itertools import permutations

def is_valid(fila, restricoes):
    if not restricoes:
        return True
    
    for r in restricoes:
        if r[2] > 0:
            valid = abs(fila[r[0]] - fila[r[1]]) <= r[2]
        else:
            valid = abs(fila[r[0]] - fila[r[1]]) >= abs(r[2])
        
        if not valid:
            return False
    
    return True

def solve(n, restricoes):
    count = 0
    for perm in permutations(range(n)):
        if is_valid(perm, restricoes):
            count += 1
    return count

def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        restricoes = [tuple(map(int, input().split())) for _ in range(m)]
        print(solve(n, restricoes))

if __name__ == "__main__":
    main()
