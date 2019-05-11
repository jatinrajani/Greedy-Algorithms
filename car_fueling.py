# python3
import sys

def compute_min_refills(distance, tank, stops):
    # write your code here
    lastRefill=0
    numRefills=0
    currentRefill=0
    stops.append(0)
    stops.append(distance)
    
    stops.sort()
    n=int(len(stops)-2)
    while currentRefill<=n:
        lastRefill=currentRefill
        while (currentRefill<=n) and (stops[currentRefill+1]-stops[lastRefill]<=tank): 
            currentRefill+=1
        
        if currentRefill==lastRefill:
            return -1
        if currentRefill<=n:
            numRefills+=1
    return numRefills




if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
