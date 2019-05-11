#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    a.sort()
    b.sort()
    res = 0
    i=0
    while i<len(a):
        res += a[i] * b[i]
        i+=1
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
