import sys

def missing_number(lista):
    n = len(lista) + 1  # the missing number 
    expected_val = n * (n + 1) // 2 # sum of all numbers including the missing one 
    curr_value = sum(lista) # sum of numbers in the list
    missing = expected_val - curr_value 

    return missing

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    # n = int(data[0])  
    lista = list(map(int, data[1:])) 
    print(missing_number(lista))

# n = 5
# lista = [1, 2, 4, 5]
# print(missing_number(lista))

    


    