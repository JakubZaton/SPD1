import sys
from heapq import heappush, heapify, nlargest, heappop

class RPQ:

    @staticmethod
    def sort_R(tab):
        data = tab.copy()
        order_by_access_time = data.copy()
        order_by_access_time.sort(key=lambda x: x[0])
        return order_by_access_time

    @staticmethod
    def loss_function(tab):
        dane = tab.copy()
        max_time_q = dane[0][0] + dane[0][1] + dane[0][2]  # bieżący czas dostarczenia zadania
        time = dane[0][0] + dane[0][1]
        C = []
        C.append(time)
        for t in range(1, len(dane)):
            if time > dane[t][0]:
                time = time + dane[t][1]
            else:
                time = dane[t][0] + dane[t][1]

            time_q = dane[t][2] + time
            max_time_q = max(max_time_q, time_q)
            if max_time_q in C:
                C.append(time_q)
            else:
                C.append(max_time_q)
        return C

    @staticmethod
    def find_max_C(data):
        max_C = data[0]
        for i in range(0, len(data)):
            if data[i] > max_C:
                max_C = data[i]
        return max_C


    @staticmethod
    def heap(data):
        q = [(x[2], x) for x in data]
        heapify(q)
        max = nlargest(1, q)
        max_q = max[0][0]
        max_el = max[0][1]
        p = max[0][1][1]
        return max_q, max_el, p

    @staticmethod
    def schrage(tab):
        N = tab.copy()
        pi = []
        #n, N = RPQ.readData(data)  # wczytuje dane z pliku
        k = 1
        G = []
        sorted = RPQ.sort_R(N)
        min_r = sorted[0][0]
        time = sorted[0][0]  # pobieram najmniejszy czas r (korzystam z sortowania po R)
        while len(N) != 0 or len(G) != 0:
            while len(N) != 0 and (min_r <= time):
                el = sorted[0]
                heappush(G, el)  # dodaję element do G
                N.remove(el)  # usuwam element z N
                sorted.remove(el)
                if(len(sorted) != 0):
                    min_r = sorted[0][0]
            if len(G) != 0:
                max_q, el_2, p = RPQ.heap(G)
                G.remove(el_2)  # usuwam ten element z G
                time += p  # do czasu rozpoczęcia dodaję czas wykonania
                k += 1
                pi.append(el_2)
            else:
                time = sorted[0][0]
        return pi

    @staticmethod
    def schrage_pmtn(tab):
        #n, N = RPQ.readData(data)  # wczytuje dane z pliku
        N = tab.copy()
        G = []
        sorted = RPQ.sort_R(N)
        min_r = sorted[0][0]
        time = 0 # pobieram najmniejszy czas r (korzystam z sortowania po R)
        C_max = 0
        el_l = [0, 0, 1000000]
        while len(N) != 0 or len(G) != 0:
            while len(N) != 0 and min_r <= time:
                el = sorted[0]
                heappush(G, el)  #dodaję element do G
                N.remove(el)  #usuwam element z N
                sorted.remove(el)
                if (len(sorted) != 0):
                    min_r = sorted[0][0]
                if el[2] > el_l[2]:
                    el_l[1] = time - el[0]
                    time = el[0]
                    if el_l[1] > 0:
                        heappush(G, el_l)
            if len(G) == 0:
                time = sorted[0][0]
            else:
                max_q, el_2, p = RPQ.heap(G)  # wyszukuję największy czas q
                G.remove(el_2)  # usuwam ten element z G
                el_l = el_2
                time += p  # do czasu rozpoczęcia dodaję czas wykonania
                C_max = max(C_max, time + max_q)
        return C_max

    @staticmethod
    def find_max_b(data_b, C_max):
        for i in range(len(data_b)-1, 0, -1):
            if data_b[i] == C_max:
                return data_b.index(data_b[i])

    @staticmethod
    def find_min_a(data, C_max, b):
        sum_p = 0
        for i in range(0, len(data)):
            for j in range(i, b+1):
                sum_p += data[j][1]
            r = data[i][0]
            q = data[b][2]
            C_max_pom = data[i][0] + sum_p + data[b][2]
            if C_max_pom == C_max:
                return i
            sum_p = 0

    @staticmethod
    def find_max_c(data, a, b):
        for i in range(a, b): # bylo tutaj range(b, a, -1)
            if data[i][2] < data[b][2]:
                return i

    @staticmethod
    def find_new_rpq(c, b, data):
        new_p = 0
        new_r = sys.maxsize
        min_q = sys.maxsize
        new_q = 0
        for i in range(c, b+1):
            if data[i][0] < new_r:
                new_r = data[i][0]
            if data[i][1] < min_q:
                min_q = data[i][1]
            new_p += data[i][1]
        return new_r, new_p, new_q


    @staticmethod
    def carlier(J):
        tab = RPQ.schrage(J)
        old_pi = RPQ.schrage(J)
        U = RPQ.find_max_C(RPQ.loss_function(tab))
        UB = sys.maxsize
        if U < UB:
            UB = U
            new_pi = old_pi
        loss_f = RPQ.loss_function(RPQ.schrage(tab))
        C_max = RPQ.find_max_C(RPQ.loss_function(RPQ.schrage(tab)))
        b = RPQ.find_max_b(loss_f, C_max)
        a = RPQ.find_min_a(tab, C_max, b)
        c = RPQ.find_max_c(tab, a, b)
        if c == 0 or c is None:
            return new_pi
        new_r, new_p, new_q = RPQ.find_new_rpq(c, b, tab)
        r_c = tab[b][0]
        tab[b][0] = max(tab[b][0], new_r + new_p)
        LB = RPQ.schrage_pmtn(tab)
        if LB < UB:
            RPQ.carlier(tab)
        tab[b][2] = r_c
        q_c = tab[b][2]
        tab[b][2] = max(tab[b][2], new_q + new_p)
        LB = RPQ.schrage_pmtn(tab)
        if LB < UB:
            RPQ.carlier(tab)
        tab[b][2] = q_c


def readData(filepath):
    data = []
    with open(filepath) as f:
        n, kolumny = [int(x) for x in next(f).split()]
        data = [[int(x) for x in line.split()] for line in f]
    return data


wyniki_schrage = []
wyniki_schrage_pmtn = []

data10 = readData('data10.txt')
print(RPQ.loss_function(RPQ.carlier(data10)))
wyniki_schrage.append(RPQ.find_max_C(RPQ.loss_function(RPQ.schrage(data10))))
wyniki_schrage_pmtn.append(RPQ.schrage_pmtn(data10))

data20 = readData('data20.txt')
wyniki_schrage.append(RPQ.find_max_C(RPQ.loss_function(RPQ.schrage(data20))))
wyniki_schrage_pmtn.append(RPQ.schrage_pmtn(data20))

data50 = readData('data50.txt')
wyniki_schrage.append(RPQ.find_max_C(RPQ.loss_function(RPQ.schrage(data50))))
wyniki_schrage_pmtn.append(RPQ.schrage_pmtn(data50))

data100 = readData('data100.txt')
wyniki_schrage.append(RPQ.find_max_C(RPQ.loss_function(RPQ.schrage(data100))))
wyniki_schrage_pmtn.append(RPQ.schrage_pmtn(data100))

data500 = readData('data500.txt')
wyniki_schrage.append(RPQ.find_max_C(RPQ.loss_function(RPQ.schrage(data500))))
wyniki_schrage_pmtn.append(RPQ.schrage_pmtn(data500))

print(wyniki_schrage)
print(wyniki_schrage_pmtn)
