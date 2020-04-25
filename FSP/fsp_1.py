import itertools
import sys
from timeit import default_timer as timer


def czytaj(sciezka):
    el_tab = []
    parametry = []
    with open(sciezka) as f:
        n, m = [int(x) for x in next(f).split()]
        data = [[int(x) for x in line.split()] for line in f]
    for i in range(0, len(data)):
        el = data[i][1::2]
        el_tab.append(el)
    parametry.append(n)
    parametry.append(m)
    return parametry, el_tab


def calculate(data, parametry):
    S = []
    C = []
    czas_z = 0
    czas_r_tab = []
    czas_z_tab = []
    for m in range(0, parametry[1]):
        for j in range(0, parametry[0]):
            if m == 0:
                czas_r = czas_z
                czas_z = czas_r + data[j][m]
            else:
                if j == 0:
                    czas_r = C[m-1][j]
                    czas_z = czas_r + data[j][m]
                else:
                    czas_r = max(C[m-1][j], czas_z)
                    czas_z = czas_r + data[j][m]
            czas_r_tab.append(czas_r)
            czas_z_tab.append(czas_z)
        S.append(czas_r_tab)
        C.append(czas_z_tab)
        czas_r_tab = []
        czas_z_tab = []
    return C.pop().pop()


def licz_kombinacje_iteracyjnie(data, parametry):
    comb = itertools.permutations(data, len(data))
    F_wynik = sys.maxsize
    for i in comb:
        if calculate(i, parametry) < F_wynik:
            F_wynik = calculate(i, parametry)
    return F_wynik



def main():
    parametry, data = czytaj('data005.txt')
    start = timer()
    licz_kombinacje_iteracyjnie(data, parametry)
    end = timer()
    wynik = end - start
    print(wynik)


if __name__ == '__main__':
    main()

