def czytaj(filepath):
    data = []
    with open(filepath) as f:
        n, kolumny = [int(x) for x in next(f).split()]
        data = [[int(x) for x in line.split()] for line in f]
    return n, data

def modifyBit(n, p, b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)

def decimalToBinary(num):
    return bin(num).replace("0b", "")

def binaryToDecimal(num):
    return int(num, 2)

def PD_itreacyjny(n, d):
    F = []
    max_val_tab = []

    F.append(max(d[0][0] - d[0][2], 0) * d[0][1])  # pierwszy krok
    for i in range(2, 2 ** n):
        bin = decimalToBinary(i)
        for j in range(0, len(bin)):
            binary = decimalToBinary(i)
            modified = modifyBit(i, j, 0)
            modified_binary = decimalToBinary(modified)
            reversedstring = ''.join(reversed(bin))
            p = [pos for pos, char in enumerate(reversedstring) if char == '1']
            if binary != modified_binary:
                ile = 0
                for m in range(0, len(p)):
                    ile += d[p[m]][0]
                if modified == 0:
                    max_val = max(ile - d[j][2], 0) * d[j][1]
                else:
                    max_val = max(ile - d[j][2], 0) * d[j][1] + F[modified - 1]
                max_val_tab.append(max_val)
        min_val = min(max_val_tab)
        F.append(min_val)
        max_val_tab = []

    print(F.pop())


def main():
    n, d = czytaj('data18.txt')
    PD_itreacyjny(n, d)

if __name__ == '__main__':
    main()


