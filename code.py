import time
import random
import sys
import matplotlib.pyplot as plt
 

def minmult(n,d):
    M = [[0 for i in range(1, n+1)] for j in range(1, n+1)]
    p = [[0 for i in range(1, n+1)] for j in range(1, n+1)]
    for i in range(1, n):
        M[i][i] = 0
    mini,minj=0,0
    for diagonal in range(2, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal -1
            M[i][j] = sys.maxsize
            for k in range(i, j):
                q = M[i][k] + M[k + 1][j] + d[i-1]*d[k]*d[j]
                if q < M[i][j]:
                    M[i][j] = q
                    mini=i
                    minj=j
                p[i][j]=k
                     
    return mini,minj,p
    
       
def orderfunc(i,j,p):
  k=0
  if i==j:
    y=0
    print()
  else:
    k=0
    k=p[i][j]
    #print(i,j)
    print()
    orderfunc(i,k,p)
    orderfunc(k+1,j,p)
    print()




if __name__ == "__main__":
    n=[i for i in range (1,100)]
    t1arr=[]
    t2arr=[]
    for n1 in n:
      t1=time.time()
      d=[random.randint(1,100) for i in range(n1)]
      i,j,p=minmult(n1,d)
      t2=time.time()
      t3=t2-t1
      t1arr.append(t3)
      t4=time.time()

      orderfunc(i,j,p)
      t5=time.time()
      t2arr.append(t5-t4)

    plt.plot(n,t1arr,label = 'Algorithm 3.6')    
    plt.plot(n,t2arr, label = 'Algorithm 3.7')
    plt.xlabel("n")
    plt.ylabel("Time")
    plt.legend(bbox_to_anchor =(0.75, 1.15), ncol = 2)
 
