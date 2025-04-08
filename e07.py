# Téo Sobrino Alves - 12557192 ex2, Lab de Alg. Avançados

def evaluation(prices: list, target: int):

    prices.sort()
    i = 0
    j = len(prices) - 1
    sol = (0, 0)
    s = prices[i] + prices[j]
    while(i < j):
        if s > target:
            j -= 1
        if s < target:
            i += 1
        if s == target:
            sol =(prices[i], prices[j])
            i += 1
        s = prices[i] + prices[j]
        
    print(f"Joaquina deve comprar os jogos de preços {sol[0]} e {sol[1]}. \n")
    
    return

def main():

    while True:
        try:
            n = input()
        except EOFError:
            return
        if n.isalnum():
            n = int(n)
            prices = [int(x) for x in list(input().split(' ')) if x.isalnum()]
            target = int(input())
            evaluation(prices, target)

    return

if __name__ == '__main__':
    main()