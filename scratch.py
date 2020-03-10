

import numpy

class RPQ:


    @staticmethod
    #czytamy z sciezki
    def czytaj(sciezka):
        wyjscie=[]
        with open(sciezka) as f:
            f.readline() #pomijamy pierwsza linie,
            wyjscie = [[int(x) for x in line.split()] for line in f] #wyciagamy kolejne wiersze
            return wyjscie

#print(RPQ.czytaj("data10.txt"))

    @staticmethod
    def sortuj(data):  # proste sortowanie po r
        posortowane = data.copy()
        posortowane.sort(key=lambda x: x[0])
        return posortowane

    @staticmethod
    def liczC(data):
        C=[]

        maksymalny = data[0][0]+data[0][1]+data[0][2] #wczytujemy wartosci z pierwszego zadania
        #print(maksymalny)
        czas = data[0][0]+data[0][1] #sprawdzamy czas przygotowania i wykonywania pierwszego zadania
        C.append(czas) #dodajemy czas bdo listy czasow

        for x in range(1, len(data)):
                if czas > data[x][0]: #sprawdzamy czy czas wykoywania sie poprzedniego zadania jest dluzszy od czasu przygotowywania nastepnego
                    czas=czas+data[x][1] #jesli tak to dodajemy tylko czas wykonywania
                  #  print(czas)
                else:
                    czas = data[x][0]+data[x][1] # jesli nie to musimy dodac czas przygotowania i wykonywania
                  #  print(czas)
                czas2 = data[x][2] + czas # czas dostarczenia i czas porzedniego
                maksymalny = max(maksymalny,czas2) # sprawdzamy maskywmalna wartosc
                C.append((maksymalny)) #dodajemy czas do listy czasow
        return C




data =RPQ.czytaj("data500.txt")
#print(data)
print(RPQ.liczC(data))
print(RPQ.liczC(data).pop())
posortowane=RPQ.sortuj(data)
#print((posortowane))
print(RPQ.liczC(posortowane))
print(RPQ.liczC(posortowane).pop())












