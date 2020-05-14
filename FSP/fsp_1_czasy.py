import itertools
import sys
from copy import deepcopy
import random
from timeit import default_timer as timer


def czytaj(sciezka):
    data = []
    parametry = []
    with open(sciezka) as f:
        n, m = [int(x) for x in next(f).split()]
        data_pom = [[int(x) for x in line.split()] for line in f]
    for i in range(0, len(data_pom)):
        el = data_pom[i][1::2]
        data.append(el)
    parametry.append(n)
    parametry.append(m)
    return parametry, data


parametry, data = czytaj('data005.txt')
S = []
C = []

def calculate(data):
    S.clear()
    C.clear()
    J = deepcopy(data)
    czas_r_tab = []
    czas_z_tab = []
    czas_z = 0
    for m in range(0, parametry[1]):
        for j in range(0, len(data)):
            if m == 0:
                czas_r = czas_z
                czas_z = czas_r + J[j][m]
            else:
                if j == 0:
                    czas_r = C[m-1][j]
                    czas_z = czas_r + J[j][m]
                else:
                    czas_r = max(C[m-1][j], czas_z)
                    czas_z = czas_r + J[j][m]
            czas_r_tab.append(czas_r)
            czas_z_tab.append(czas_z)
        S.append(czas_r_tab)
        C.append(czas_z_tab)
        czas_r_tab = []
        czas_z_tab = []
    return C[-1][-1]


def licz_kombinacje_iteracyjnie(data):
    comb = itertools.permutations(data, len(data))
    C_wynik = sys.maxsize
    for i in comb:
        wynik = calculate(i)
        if wynik < C_wynik:
            C_wynik = wynik
    return C_wynik


def johnson(data, parametry):
    l = 0
    k = parametry[0] - 1
    pi = [0] * parametry[0]
    while len(data) != 0:
        min_val = min(data, key=min)
        if min_val[0] < min_val[1]:
            pi[l] = min_val
            l = l + 1
        else:
            pi[k] = min_val
            k = k - 1
        data.remove(min_val)
    return pi


def bound_1(pi):
    max_tab = []
    calculate(pi)
    for i in range(0, parametry[1]):
        sum_p = 0
        C_max = C[i][len(pi)-1]
        for j in range(0, parametry[0]):
            if data[j] not in pi:
                sum_p = sum_p + data[j][i]
        max_tab.append(C_max + sum_p)
    LB = max(max_tab)
    return LB


def bound_2(pi):
    max_tab = []
    sum_min = []
    calculate(pi)
    suma = 0
    for i in range(0, parametry[1]):
        sum_p = 0
        C_max = C[i][len(pi) - 1]
        for m in range(i, parametry[1]):
            for j in range(0, parametry[0]):
                if m != i:
                    sum_min.append(data[j][m])
                if data[j] not in pi:
                    if i == m:
                        sum_p = sum_p + data[j][m]
            if len(sum_min) != 0:
                min_val = min(sum_min)
                suma = suma + min_val
                sum_min.clear()
        max_tab.append(C_max + sum_p + suma)
        suma = 0
    LB = max(max_tab)
    return LB


def bound_3(pi):
    max_tab = []
    sum_min = []
    calculate(pi)
    suma = 0
    for i in range(0, parametry[1]):
        sum_p = 0
        C_max = C[i][len(pi) - 1]
        for m in range(i, parametry[1]):
            for j in range(0, parametry[0]):
                if data[j] not in pi:
                    if i == m:
                        sum_p = sum_p + data[j][m]
                    if i > m:
                        sum_min.append(data[j][m])
            if len(sum_min) != 0:
                min_val = min(sum_min)
                suma = suma + min_val
                sum_min.clear()
        max_tab.append(C_max + sum_p + suma)
        suma = 0
    LB = max(max_tab)
    return LB


def bound_4(pi):
    max_tab = []
    suma_tab = []
    sum_min = 0
    calculate(pi)
    for i in range(0, parametry[1]):
        suma_tab.clear()
        sum_p = 0
        C_max = C[i][len(pi) - 1]
        for m in range(i, parametry[1]):
            for j in range(0, parametry[0]):
                if data[j] not in pi:
                    if i == m:
                        sum_p = sum_p + data[j][m]
                    if i > m:
                        sum_min = sum_min + data[j][m]
            if m != i:
                suma_tab.append(sum_min)
                sum_min = 0
        if len(suma_tab) != 0:
            suma = min(suma_tab)
        else:
            suma = 0
        max_tab.append(C_max + sum_p + suma)
    LB = max(max_tab)
    return LB


count = 0
def prodecure_BnB():
    N = deepcopy(data)
    pi = []
    for j in N:
        UB = BnB(j, pi, N)
        global count
        count = count + 1
    print("Rekurencyjna liczba wywołań: {}".format(count))
    return UB


UB = sys.maxsize
#UB = random.randint(0, sys.maxsize)
def BnB(j, pi_copy, J):
    N = deepcopy(J)
    pi = deepcopy(pi_copy)
    pi.append(j)
    N.remove(j)
    if len(N) != 0:
        #LB = bound_1(pi)
        #LB = bound_2(pi)
        #LB = bound_3(pi)
        LB = bound_4(pi)
        global UB
        if LB <= UB:
            for j in N:
                UB = BnB(j, pi, N)
                global count
                count = count + 1
    else:
        C_max = calculate(pi)
        if C_max < UB:
           UB = C_max
    return UB


def main():
    #print(calculate(data))
    #print(C)
    wynik = 0
    for i in range(1):
        start = timer()
        print(prodecure_BnB())
        #prodecure_BnB()
        end = timer()
        wynik = wynik + (end - start)
    print(wynik / 1)
    #print(calculate(data))
    #pi = johnson(data, parametry)
    #print(calculate(pi))
    #licz_kombinacje_iteracyjnie(data, parametry)


if __name__ == '__main__':
    main()

