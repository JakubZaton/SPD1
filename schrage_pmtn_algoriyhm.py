class RPQ:

    @staticmethod #wczytywanie z pliku
    def readData(filepath):
        data = []
        with open(filepath) as f:
            n, kolumny = [int(x) for x in next(f).split()]
            data = [[int(x) for x in line.split()] for line in f]
        return n, data

    @staticmethod
    def sort_R(data):
        order_by_access_time = data.copy()
        order_by_access_time.sort(key=lambda x: x[0])
        return order_by_access_time

    @staticmethod
    def find_maxq_and_p(data):
        max = 0
        el = []
        p = 0
        for i in range(0, len(data)):
            if data[i][2] > max:
                max = data[i][2]
                el = data[i]
                p = data[i][1]
        return max, el, p

    @staticmethod
    def schrage_pmtn(data):
        n, N = RPQ.readData(data)  # wczytuje dane z pliku
        # k = 1
        G = []
        sorted = RPQ.sort_R(N)
        min_r = sorted[0][0]
        time = 0  # pobieram najmniejszy czas r (korzystam z sortowania po R)
        C_max = 0
        el_l = [0, 0, 1000000]
        while len(N) != 0 or len(G) != 0:
            while len(N) != 0 and min_r <= time:
                el = sorted[0]
                G.append(el)  # dodaję element do G
                N.remove(el)  # usuwam element z N
                if (len(N) != 0):
                    sorted = RPQ.sort_R(N)
                    min_r = sorted[0][0]
                if el[2] > el_l[2]:
                    el_l[1] = time - el[0]
                    time = el[0]
                    if el_l[1] > 0:
                        G.append(el_l)
            if len(G) == 0:
                # sorted = RPQ.sort_R(N)
                time = sorted[0][0]
            else:
                max_q, el_2, p = RPQ.find_maxq_and_p(G)  # wyszukuję największy czas q
                G.remove(el_2)  # usuwam ten element z G
                el_l = el_2
                time += p  # do czasu rozpoczęcia dodaję czas wykonania
                # print(time + max_q)
                C_max = max(C_max, time + max_q)
                # print(C_max)
                # pi.append(el_l)
        return C_max

#print(RPQ.loss_function(RPQ.schrage('in50.txt')).pop())
#print(RPQ.loss_function(RPQ.schrage_pmtn('in50.txt')).pop())
print(RPQ.schrage_pmtn('data10.txt'))

