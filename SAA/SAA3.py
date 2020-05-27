


import os
import re
import random
import math
from copy import deepcopy
import numpy as np


def Cmax(data):
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


def czytaj(sciezka):
    data = []
    parametry = []
    with open(sciezka) as f:
        nazwa = f.readline()
        n, m = [int(x) for x in next(f).split()]
        data_pom = [[int(x) for x in line.split()] for line in f]
    for i in range(0, len(data_pom)):
        el = data_pom[i][1::2]
        data.append(el)
    parametry.append(n)
    parametry.append(m)
    return nazwa, parametry, data


def saa(T0, Te, L):
    nazwa, parametry, data = czytaj('ta001.txt')
    T=T0
    pi=
    Tend=Te
    alpha=0.97
    cmax = Cmax(pi)
    pi_star = pi
    cmax_star = Cmax(pi_star)
    while T > Tend:
        for k in range(1, int(L)):
            pi_new = deepcopy(pi)
            i = random.randint(0, parametry[0] - 1)
            j = random.randint(0, parametry[0] - 1)
            pi_new[i], pi_new[j] = pi_new[j], pi_new[i]
            new_cmax = Cmax(pi_new)
            if new_cmax[0] > cmax[0]:
                r = random.random()
                if r >= math.e ** ((cmax[0] - new_cmax[0]) / T):
                    pi_new = pi
                    new_cmax = cmax
            pi = pi_new
            cmax = new_cmax
            if cmax[0] < cmax_star[0]:
                pi_star = deepcopy(pi)
                cmax_star = deepcopy(cmax)
    T = T*alpha
    print(cmax_star)


def main():
    saa(100, 10, 64, "swap")

if __name__ == "__main__":
    main()