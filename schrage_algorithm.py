class RPQ:

    @staticmethod
    def readData(filepath):
        data = []
        with open(filepath) as f:
            n, kolumny = [int(x) for x in next(f).split()]
            data = [[int(x) for x in line.split()] for line in f]
        return n, data

    @staticmethod
    def sort_R(data):
        posortowane = data.copy()
        posortowane.sort(key=lambda x: x[0])
        return posortowane

    @staticmethod
    def find_min(data):
        min = 1000
        el = []
        for i in range(0, len(data)):
            if data[i][0] < min:
                min = data[i][0]
                el = data[i]
        return min, el

    @staticmethod
    def find_maxq_and_p(data):
        max = 0
        el = []
        p = 0
        for i in range(0, len(data)):
            if data[i][2] > max:
                max = data[i][2]
                # print(max)
                el = data[i]
                p = data[i][1]
        return max, el, p

    @staticmethod
    def schrage(data):
        pi = 0
        n, data = RPQ.readData(data)  # wczytuje dane z pliku
        sorted = RPQ.sort_R(data)
        time = sorted[0][0]  # pobieram najmniejszy czas r (korzystam z sortowania po R)

        k = 1
        G = []
        N = data  # G - zbiór pusty, N - przypisanie wszystkich zadań
        minr, el = RPQ.find_min(N)  # pobieram najmniejszy czas r z tablicy N oraz element, który ten czas zawiera
        while len(N) != 0 or len(G) != 0:
            while len(N) != 0 and sorted[0][0] <= time:
                G.append(el)  # dodaję element do G
                N.remove(el)  # usuwam element z N
                minr, el = RPQ.find_min(N)
            if len(G) != 0:
                max_q, el_2, p = RPQ.find_maxq_and_p(G)  # wyszukuję największy czas q, element, który temu odpowiada oraz czas wykonania tego zadania
                print(el_2)
                G.remove(el_2)  # usuwam ten element z G
                time += p  # do czasu rozpoczęcia dodaję czas wykonania
                k += 1
                pi += max_q
            else:
                time = RPQ.find_min(N)
        return pi


print(RPQ.schrage('data10.txt'))

# n, data = RPQ.readData('data10.txt')
# M = []
# m, M, y = RPQ.find_maxq_and_p(data)
# print(m, M, y)
# G = [[84, 13, 103], [1, 1, 1]]
# x, y, z = RPQ.find_maxq_and_p(G)
# print(x, y, z)
