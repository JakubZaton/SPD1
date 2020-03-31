import itertools
import sys

class WiTi:

    @staticmethod
    def czytaj(sciezka):
        with open(sciezka) as f:
            n = f.readline()
            wyjscie = [[int(x) for x in line.split()] for line in f]
        return wyjscie

    @staticmethod
    def sortujD(data):
        posortowane = data.copy()
        posortowane.sort(key=lambda x: x[2])
        return posortowane

    @staticmethod
    def funkcjeCelu(data):
        S = []
        C = []
        T = []
        F = []
        S.append(0)
        el = 0
        for i in range(0, len(data) - 1):
            el += data[i][0]
            S.append(el)
        el = 0
        for i in range(0, len(data)):
            el += data[i][0]
            C.append(el)
        for i in range(0, len(C)):
            if C[i] > data[i][2]:
                T.append(C[i] - data[i][2])
            else:
                T.append(0)
        F_wynik = 0
        for i in range(0, len(C)):
            F.append(T[i] * data[i][1])
            F_wynik += F[i]
        return F_wynik

    @staticmethod
    def licz_kombinacje(data):
        comb = itertools.permutations(data, len(data))
        F_wynik = sys.maxsize
        for i in list(comb):
            if WiTi.funkcjeCelu(i) < F_wynik:
                F_wynik = WiTi.funkcjeCelu(i)
        return F_wynik

    @staticmethod
    def licz_kombinacje_rekursywnie(data):
        F_wynik = sys.maxsize
        if len(pom) == len(data):
            F_wynik2 = WiTi.funkcjeCelu(pom)
            if F_wynik2 < F_wynik:
                F_wynik = F_wynik2
        for z in data:
            temp = pom + z
            WiTi.licz_kombinacje_rekursywnie(temp)
        return F_wynik


#print(WiTi.funkcjeCelu(WiTi.sortujD(WiTi.czytaj('data11.txt'))))
#print(WiTi.licz_kombinacje(WiTi.czytaj('data5.txt')))
print(WiTi.licz_kombinacje_rekursywnie(WiTi.czytaj('data5.txt')))
