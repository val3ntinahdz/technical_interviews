import sys

def find_longest_repetition(sequence): 
    max_len = 0 # store the longest repetition 
    current_len = 1 # the length of the current repetition 
    current_char = sequence[0]

    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            current_len = current_len +1 
        else:
            max_len = max(max_len, current_len)
            current_char = sequence[i] 
            current_len = 1

    max_len = max(max_len, current_len)

    return max_len

if __name__ == "__main__":
    data = sys.stdin.read()
    sequence = list(map(str, data))  
    print(find_longest_repetition(sequence))



