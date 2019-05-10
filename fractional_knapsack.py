# Uses python3
import sys
from decimal import Decimal

def get_optimal_value(capacity, weights, values):
    value=0
    a=insertlist(weights,values)	
    while capacity!=0:
        j=getmax(a)
        c=min(weights[j[0]],capacity)
        capacity-=c
        value+=c*j[1]
        a[j[0]]=0
    return value







def insertlist(weights,values):
    a=[]
    for i in range(len(weights)):
        k=float(values[i]/weights[i])
        a.append(k)
    return(a)
	
def getmax(a):
    i=0
    r=0
    j=0
    while i<len(a):
        
        if a[i]>r:
            r=a[i]
            j=i
        i+=1
    return(j,r)
    
	
	    
	
            	       
	
	      
	
	
    
	
	           




   
    


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
