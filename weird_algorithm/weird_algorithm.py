import sys 

def weird_algorithm(n):
    sequence = []
    sequence.append(n)

    while n != 1: 
        if n % 2 == 0: 
            n = n // 2
        else: 
            n = n * 3 + 1
        sequence.append(n)

    return ' '.join(map(str, sequence))

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    n = int(data[0])  
    print(weird_algorithm(n))



