# Uses python3
import sys
b=[1,5,10]
def maxvalues(a,b):
    i=0
    d={}
    while i<len(b):
        j=int(a/b[i])
        d[b[i]]=j
        i+=1
       	
    return d

def minimum(a,b):
	i=0
	r=200000000000000
	j=0
	while i<len(b):
		if a[b[i]]!=0 and a[b[i]]<r:
			r=a[b[i]]
			j=b[i]
		i+=1
	return (j,r)


def get_change(m):
    #write your code here
    coins=0
    b=[1,5,10]
    while m!=0:
        d=maxvalues(m,b)
        x=minimum(d,b)
        coins+=x[1]
        m=m-x[0]*x[1]
    return coins
        
    

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))




