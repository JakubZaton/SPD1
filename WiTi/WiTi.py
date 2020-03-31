
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
        Spi = 0
        Cpi = []
        T = 0
        for x in range(0, len(data)):
            Cpi[x] = Spi + data[x][0]
            if Cpi[x] > data[x][2]:
                T = T + ((Cpi[x] - data[x][2]) * data[x][1])
            suma = suma + Cpi[x]
            Spi = Cpi[x]
        return T

data = WiTi.funkcjeCelu(WiTi.sortujD(WiTi.czytaj('data10.txt')))
print(data)