# Téo Sobrino Alves - 12557192 ex2, Lab de Alg. Avançados
def main():
    s = input().split(' ')
    start = 0
    consumption = 100.0/float(s[-1])
    mt = 0.0
    max_mt = 0.0
    n_leaks = 0
    init_c = consumption

    s = input().split(' ')
    while(s[-1] != '0'):

        iid = s[1]
        if(iid[0] == 'C'):
            mt += (float(s[0]) - start)/consumption
            start = float(s[0])
            consumption = 100.0/float(s[-1])
            init_c = consumption
            consumption = 1/((1/consumption) + n_leaks)

        if(iid[0] == 'V'):
            mt += (float(s[0]) - start)/consumption
            start = float(s[0])
            consumption = 1/((1/consumption) + 1)
            n_leaks += 1
        
        if(iid[0] == 'P'):
            mt += (float(s[0]) - start)/consumption
            start = float(s[0])
            if mt > max_mt:
                max_mt = mt
            mt = 0.0
        
        if(iid[0] == 'M'):
            mt += (float(s[0]) - start)/consumption
            start = float(s[0])
            consumption = init_c
            n_leaks = 0

        if(iid[0] == 'D'):
            mt += (float(s[0]) - start)/consumption
            print('%.3f' %max(mt, max_mt))
            mt = 0.0
            max_mt = 0.0
            n_leaks = 0
            start = 0

        s = input().split(' ')

    return

if __name__ == "__main__":
    main()