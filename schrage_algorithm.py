class RPQ:

    @staticmethod #wczytywanie z pliku
    def czytaj(filepath):
        data = []
        with open(filepath) as f:
            n, kolumny = [int(x) for x in next(f).split()]
            data = [[int(x) for x in line.split()] for line in f]
        return n, data

    @staticmethod
    def find_min_r(data):
        min = 100000
        el = []
        r = 0
        for i in range(0, len(data)):
            if data[i][0] < min:
                min = data[i][0]
                el = data[i]
                r = data[i][0]

        return el, r

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
    def loss_function(data):
        max_time_q = sum(data[0])  # bieżący czas dostarczenia zadania
        time = data[0][0] + data[0][1]
        C = []
        C.append(time)
        for t in range(1, len(data)):
            if time > data[t][0]:
                time = time + data[t][1]
            else:
                time = data[t][0] + data[t][1]

            time_q = data[t][2] + time
            max_time_q = max(max_time_q, time_q)
            C.append(max_time_q)
        return C

    @staticmethod
    def schrage(data):
        pi = []
        N = []
        n, N = RPQ.czytaj(data)  # wczytuje dane z pliku
        k = 1
        G = []
       # sorted = RPQ.sortujR(N)
        el3, min_r = RPQ.find_min_r(N)
        el3, time = RPQ.find_min_r(N)  # pobieram najmniejszy czas r (korzystam z sortowania po R)
        while len(N) != 0 or len(G) != 0:
            while len(N) != 0 and (min_r <= time):
                #el = sorted[0]
                G.append(el3)  # dodaję element do G
                N.remove(el3)  # usuwam element z N
                if len(N) != 0:
                    #sorted = RPQ.sortujR(N)
                    el3, min_r = RPQ.find_min_r(N)
            if len(G) != 0:
                max_q, el_2, p = RPQ.find_maxq_and_p(G)  # wyszukuję największy czas q
                #print(el_2)
                G.remove(el_2)  # usuwam ten element z G
                time += p  # do czasu rozpoczęcia dodaję czas wykonania
                k += 1
                pi.append(el_2)
            else:
               # RPQ.sortujR(N)
                el3, time = RPQ.find_min_r(N)
        return pi


print(RPQ.loss_function(RPQ.schrage('data10.txt')).pop())





