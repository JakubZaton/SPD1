import os
import re
import random
import math
from copy import deepcopy
import numpy as np

def kolejnosc(lista):
    y = []
    m = len(lista[0]) - 1
    for item in lista:
        y.append(item[m])
    return y


def graf_rozwiazania(tab):
    g = []
    n = len(tab)
    m = len(tab[0]) - 1
    for i in range(0, m):
        g.append([])
        for j in range(0, n):
            g[i].append(tab[j][i])
    return g

def pobierz_dane(plik):
    """
    Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv
    do zapisania w tabeli.
    """
    dane = []  # deklarujemy pustą listę
    if os.path.isfile(plik):  # sprawdzamy czy plik istnieje na dysku
        with open(plik, "r") as zawartosc:  # otwieramy plik do odczytu
            # i = 0
            for linia in zawartosc:
                linia = linia.replace("\n", "")  # usuwamy znaki końca linii
                linia = linia.replace("\r", "")  # usuwamy znaki końca linii
                linia = re.sub(' +', ' ', linia)  # zamieniamy wiecej niz 1 spacje na pojedyncza
                linia = linia.lstrip()  # usuwamy pierwsza spacje
                # x =  map(int, linia.split(" "))
                # x = list(x)                      # tutaj takie wygibasy żeby dodać czwarta liczbę
                # x.append(i)                      # która jest kolejnością zadań
                dane.append(list(map(int, linia.split(" "))))  # dodajemy elementy do tupli a tuplę do listy
                # i = i + 1                        # i++ zadania są numerowane od 1 do n
    else:
        print("Plik z danymi", plik, "nie istnieje!")
    return list(dane)  # przekształcamy listę na tuplę i zwracamy ją

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



def Cmax(tab):
    G = graf_rozwiazania(tab)
    n = len(tab)
    m = len(tab[0]) - 1
    C = np.zeros(shape=[len(G), len(G[0])])
    S = np.zeros(shape=[len(G), len(G[0])])  # C i S zerowe macierze o rozmiarach takich jak G
    for i in range(0, m):
        for j in range(0, n):
            S[i][j] = max(C[i][j - 1], C[i - 1][j])
            C[i][j] = S[i][j] + G[i][j]
    return [C[m - 1][n - 1], kolejnosc(tab)]


def saa(T0, Tend, L, metoda):
    x = T0 / (10 ** 3)  # tu wpisujemy metode liczenia x
    T = T0
    pi= []
    alfa = 0.97
    N = pobierz_dane('data001.txt')
    n = N[0][0]
    m = N[0][1]

    i=0
    for item in N:
        # self.pi.append([Node(item), i])
        pi.append(item[1::2])
        pi[pi.index(item[1::2])].append(i)
        i += 1
    cmax = Cmax(pi)
    pi_star = pi
    cmax_star = Cmax(pi_star)
    while T > Tend:
        for k in range(1, int(L)):
            pi_new = deepcopy(pi)
            i = random.randint(0, n - 1)
            if metoda == "adj":
                if i < n - 1:
                    pi_new[i], pi_new[i + 1] = pi_new[i + 1], pi_new[i]
                else:
                    pi_new[i], pi_new[i - 1] = pi_new[i - 1], pi_new[i]
            else:
                j = random.randint(0, n - 1)
                pi_new[i], pi_new[j] = pi_new[j], pi_new[i]
            new_cmax = Cmax(pi_new)
            # print("pi",self.pi,"pi_new", pi_new, i, j)
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
            # self.T -= x                 # tu wybieramy schemat chlodzenia
        T = T * alfa





'''class SAA:
    """Klasa realizująca algorytm symulowanego wyżarzania"""

    def __init__(self, plik, metoda):
        N = pobierz_dane(plik)
        self.pi = []
        self.n = N[0][0]
        self.m = N[0][1]
        self.metoda = metoda
        N.remove(N[0])
        i = 0
        for item in N:
            # self.pi.append([Node(item), i])
            self.pi.append(item[1::2])
            self.pi[self.pi.index(item[1::2])].append(i)
            i += 1
        self.cmax = Cmax(self.pi)
        self.pi_star = self.pi
        self.cmax_star = Cmax(self.pi_star)
        self.T = 0
        self.alfa = 0.97  # tu wpisujemy wartość alfa
        self.saa(10 ** 4, 10, self.n ** 2)  # math.sqrt(self.n)) # tu wpisujemy z jakimi parametrami uruchomić algorytm
        # T0, Tend, L
        print(self.cmax_star)'''




def main():
    saa(100, 10, 64, "swap")

if __name__ == "__main__":
    main()