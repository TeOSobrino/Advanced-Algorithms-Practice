# Téo Sobrino Alves -- 12557192 - Lab de Alg Av. - ex 4
# N dias 
# Preço para cada dia
# K Orçamento total

import numpy as np

def sol(k:int, prices:list):

    ref_prices = list(zip(prices, [x+1 for x in range(0, len(prices))]))
    ref_prices = sorted(ref_prices)
    
    num_stocks = 0
    for a in ref_prices:
        total_price = a[0]*a[1] 
        if total_price <= k:
            k -= total_price
            num_stocks += a[1]
        else:
            max_buyout = int(k/a[0])
            k -= max_buyout * a[0]
            num_stocks += max_buyout
    print(num_stocks)
        
    return

if __name__ == '__main__' :
    n = int(input())
    prices = list(map(int, input().split(' ')))
    k = int(input())

    sol(k, prices)