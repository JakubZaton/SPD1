from heapq import heappush, heapify, nlargest, heappop

from timeit import default_timer as timer
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
    def heap(data):
        q = [(x[2], x) for x in data]
        heapify(q)
        # print(q)
        max = nlargest(1, q)
        max_q = max[0][0]
        max_el = max[0][1]
        p = max[0][1][1]
        return max_q, max_el, p

    @staticmethod
    def schrage(data):

        pi = []
        n, N = RPQ.readData(data)  # wczytuje dane z pliku
        k = 1
        G = []
        sorted = RPQ.sort_R(N)
        min_r = sorted[0][0]
        time = sorted[0][0]  # pobieram najmniejszy czas r (korzystam z sortowania po R)
        start = timer()
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
        end = timer()
        return end - start  # pi - zeby liczyl pi

    @staticmethod
    def schrage_pmtn(data):

        n, N = RPQ.readData(data)  # wczytuje dane z pliku
        G = []
        sorted = RPQ.sort_R(N)
        min_r = sorted[0][0]
        time = 0 # pobieram najmniejszy czas r (korzystam z sortowania po R)
        C_max = 0
        el_l = [0, 0, 1000000]
        start = timer()
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
        end = timer()
        return end - start  # C_max bylo
'''

Wyniki samych algorytmow

wyniki_schrage = []
wyniki_schrage_pmtn = []

wyniki_schrage.append(RPQ.loss_function(RPQ.schrage('data10.txt')).pop())
wyniki_schrage.append(RPQ.loss_function(RPQ.schrage('data20.txt')).pop())
wyniki_schrage.append(RPQ.loss_function(RPQ.schrage('data50.txt')).pop())
wyniki_schrage.append(RPQ.loss_function(RPQ.schrage('data100.txt')).pop())
wyniki_schrage.append(RPQ.loss_function(RPQ.schrage('data500.txt')).pop())
print(wyniki_schrage)
wyniki_schrage_pmtn.append(RPQ.schrage_pmtn('data10.txt'))
wyniki_schrage_pmtn.append(RPQ.schrage_pmtn('data20.txt'))
wyniki_schrage_pmtn.append(RPQ.schrage_pmtn('data50.txt'))
wyniki_schrage_pmtn.append(RPQ.schrage_pmtn('data100.txt'))
wyniki_schrage_pmtn.append(RPQ.schrage_pmtn('data500.txt'))
print(wyniki_schrage_pmtn)

J = [[1,4,4],[2,3,3],[3,10,7]]
my_queue = []
for item in range(0,len(J)):
  heappush(my_queue,(J[item][2],J[item]))
my_queue.reverse()
print(my_queue)
while my_queue:
    x = heappop(my_queue)
    print(x)

'''

#czas algorytmow


wynikschrange10 =0
for i in range(100):
    wynikschrange10 = wynikschrange10 + RPQ.schrage('data10.txt')
print(wynikschrange10/100)

wynikschrange20 =0
for i in range(100):
    wynikschrange20 = wynikschrange20 + RPQ.schrage('data20.txt')
print(wynikschrange20/100)

wynikschrange50 =0
for i in range(100):
    wynikschrange50 = wynikschrange50 + RPQ.schrage('data50.txt')
print(wynikschrange50/100)

wynikschrange100 =0
for i in range(100):
    wynikschrange100 = wynikschrange100 + RPQ.schrage('data100.txt')
print(wynikschrange100/100)

wynikschrange200 =0
for i in range(100):
    wynikschrange200 = wynikschrange200 + RPQ.schrage('data200.txt')
print(wynikschrange200/100)

wynikschrange500 =0
for i in range(100):
    wynikschrange500 = wynikschrange500 + RPQ.schrage('data500.txt')
print(wynikschrange500/100)

'''
wynikschrange10 =0
for i in range(100):
    wynikschrange10 = wynikschrange10 + RPQ.schrage_pmtn('data10.txt')
print(wynikschrange10/100)

wynikschrange20 =0
for i in range(100):
    wynikschrange20 = wynikschrange20 + RPQ.schrage_pmtn('data20.txt')
print(wynikschrange20/100)

wynikschrange50 =0
for i in range(100):
    wynikschrange50 = wynikschrange50 + RPQ.schrage_pmtn('data50.txt')
print(wynikschrange50/100)

wynikschrange100 =0
for i in range(100):
    wynikschrange100 = wynikschrange100 + RPQ.schrage_pmtn('data100.txt')
print(wynikschrange100/100)

wynikschrange200 =0
for i in range(100):
    wynikschrange200 = wynikschrange200 + RPQ.schrage_pmtn('data200.txt')
print(wynikschrange200/100)

wynikschrange500 =0
for i in range(100):
    wynikschrange500 = wynikschrange500 + RPQ.schrage_pmtn('data500.txt')
print(wynikschrange500/100)
'''