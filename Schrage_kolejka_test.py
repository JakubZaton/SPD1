
import heapq
import numpy
import pandas
import pandas as pd

class RPQ:

    @staticmethod #wczytywanie z pliku
    def czytaj(filepath):
        data = []
        with open(filepath) as f:
            n, kolumny = [int(x) for x in next(f).split()]
            data = [[int(x) for x in line.split()] for line in f]
        return n, data
   # @staticmethod
   # def czytaj2(filepath):
   #     data2=[]
   #     with open(filepath) as f:
   #         n, kolumny = [int(x) for x in next(f).split()]
   #         data = [[int(x) for x in line.split()] for line in f]
    #    data2 = pd.DataFrame(data)
   #     return data2


    @staticmethod
    def sortujR(data):
        posortowane = data.copy()
        posortowane.sort(key=lambda x: x[0])
        return posortowane

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
        #N2 = RPQ.czytaj2(data)
        k = 0
        i = -1
        G = [[0,0,0]]
        pomocnicza=0;
        sorted = RPQ.sortujR(N)
        min_r = sorted[0][0]
        time = sorted[0][0]  # pobieram najmniejszy czas r (korzystam z sortowania po R)

        while len(N) != 0 or len(G) != 0:
            while len(N) != 0 and (min_r <= time):
                if len(G) ==0:
                    G = [[0, 0, 0]]
                el = sorted[0]
                for z in range(len(G)):
                    if G[z][2] < el[2]:
                        if G == [[0, 0, 0]]:
                            G.pop(0)
                        G.insert(z, el)  # dodaję element do G
                #heapq.heappush(G, el)
                #print(G)

                N.remove(el)  # usuwam element z N
                sorted.remove(el)
                if len(N) != 0:
                   # sorted = RPQ.sortujR(N)
                    min_r = sorted[0][0]

            if len(G) != 0:
              #  G2 = pd.DataFrame(G)
              #  print(G2)
               # Maxq = G2.nlargest(1, 2)
              #  max_q = Maxq[2]
               # el_2 = Maxq
               # p = Maxq[1]
               # max_q, el_2, p = RPQ.find_maxq_and_p(G)  # wyszukuję największy czas q

                el_2 = G.pop(-1)
                max_q = el_2[2]
                p = el_2[1]
                #el_2 = heapq.nlargest(1, G, key=G[0][2])
                #print(el_2)
               # G.remove(el_2)  # usuwam ten element z G
                #heapq._heappop_max(G)
                time += p  # do czasu rozpoczęcia dodaję czas wykonania
                k += 1
                pi.append(el_2)
            else:
                #RPQ.sortujR(N) #nie potrzebne
                time = sorted[0][0]

        return pi


#print(RPQ.czytaj2('data10.txt'))

print(RPQ.loss_function(RPQ.schrage('data10.txt')).pop())
