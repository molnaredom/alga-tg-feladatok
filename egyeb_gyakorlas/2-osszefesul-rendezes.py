import math
import sys
"""
a fgv elvárja h [p..q] és [q+1..r] résztömbök rendezettek legyenek
ordó(n) idejű ahol n =r-p+1 (az első résztömb kezdete - a második résztömb vége +1)

"""

def osszefesul(A,p,q,r):
    n1 = q-p+1  #[p..q] hossza n1 = q-p+1 - plusz 1 azért kell mert 0. elem is egy elem tehát 2-0 = 3 nak kéne lennie mert 0,1,2
    n2= r-q #[q+1..r] hossza
    L= [i for i in range(0,n1+1)] #bal = Left , +1 az őrszemek
    R=[i for i in range(0,n2+1)] # jobb = Right +1 az őrszemek
    for i in range(0,n1):
        L[i] = A[p+i]
    for j in range(0,n2):
        R[j] = A[q+j+1]
    L[n1] =sys.maxsize # őrszemek
    R[n2] =sys.maxsize

    i=0
    j=0
    for k in range(p,r+1):# teljes intervallum amiben dolgozunk
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j= j+1
    #return A


def osszefesulo_rendezes(A, p,r):
    if p< r:
        q = math.floor((p+r)/2)
        osszefesulo_rendezes(A,p,q)
        osszefesulo_rendezes(A,q+1,r)
        osszefesul(A,p,q,r)




A = [8,7,6,5,4,3,2,1]
print(osszefesulo_rendezes(A,0,len(A)))



