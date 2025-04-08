# Téo Sobrino Alves -- 12557192 - Lab de Alg Av. - ex 4
# N dias
# M tarefas
# Deadline para cada tarefa
# serão necessários teto(M/N) robos
# cada robo deve selecionar a tarefa com menor deadline primeiro

import math
import numpy as np

def sol(num:int, dates:list):

    day_completed = [0]*len(dates)
    bot_assigned  = [0]*len(dates)
    #obtemos a ordem de cada número
    ref_day = np.argsort(np.array(dates))
    day = 1

    #são feitos os piso(m/n_robos) desígnios de tarefas 
    for i in range(0, len(ref_day)-num, num):
        for j in range(num):
            day_completed[ref_day[i+j]] = day
            bot_assigned[ref_day[i+j]] = j+1
        day += 1        

    # devemos então fazer o desígnio das tarefas restantes, notando que haverão
    # no máximo n_robos tarefas
    bot = 1    
    for i in range(0, len(ref_day)):
        if(day_completed[i] == 0):
            day_completed[i] = day
            bot_assigned[i] = bot
            bot += 1
    
    print(f'{num}')
    for day, bot in zip(day_completed, bot_assigned):
        print(f'{day} {bot}')
    return

if __name__ == '__main__' :
    n = int(input())
    m = int(input())
    dates = list(map(int, input().split(' ')))
    sol(int(math.ceil(m/n)), dates)