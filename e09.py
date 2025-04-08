# Téo Sobrino Alves - 12557192 ex2, Lab de Alg. Avançados
# ex9

def is_valid(digit_set, b, N):
    used = [False] * 10
    a = b * N
    
    for i in digit_set:
        used[i] = True
    
    s = str(a)
    if len(s) > 5:
        return False
    
    for char in s:
        k = int(char)
        if used[k]:
            return False
        used[k] = True
    
    return True

def solve(digit_set, used, N, solutions):
    if len(digit_set) == 5:
        b = sum(digit_set[i] * (10 ** i) for i in range(5))
        if is_valid(digit_set, b, N):
            solutions.append((b * N, b))
        return
    
    for i in range(10):
        if used[i]:
            continue
        if len(digit_set) == 5:
            return
        digit_set.append(i)
        used[i] = True
        solve(digit_set, used, N, solutions)
        digit_set.pop()
        used[i] = False

def main():
    while True:
        N = int(input())
        if N == 0:
            break
        
        solutions = []
        digit_set = []
        used = [False] * 10
        
        solve(digit_set, used, N, solutions)
        
        if not solutions:
            print(f"Não há soluções para {N}.")
        else:
            solutions.sort()
            for sol in solutions:
                print(f"{sol[0]} / {sol[1]} = {N}")
        
        print()

if __name__ == "__main__":
    main()