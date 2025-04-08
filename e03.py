# Téo Sobrino Alves -- 12557192 - Lab de Alg Av. - ex 4
# N doces
# A cada compra K grátis 
# Preço doces
# Ordenar o preço
# cada compra nos dará 1 + K doces, logo, teremos N/(1+K) compras
# selecionar a soma dos (N/(K+1)) maiores e menores valores de preço 
import math
def sol(num:int, prices:list):
    if(num <= 0): num = 1
    prices.sort()

    mx = 0
    mn = 0
    sz = len(prices) - 1
    for i in range(0, num):
        mx += prices[sz - i]
        mn += prices[i]
    print(f'{mn} {mx}')

    return

if __name__ == '__main__' :
    n = int(input())
    k = int(input())
    p = list(map(int, input().split(' ')))
    sol(int(math.ceil(n/(k+1))), p)