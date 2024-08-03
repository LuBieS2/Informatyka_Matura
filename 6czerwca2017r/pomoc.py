def sitko(n):
    czyjest=[]
    for l in range(n):
        czyjest.append(0)
    j=1
    while j*j<n:
        j+=1
    print(j)
    for i in range(2,j+1):
        print(i)
        kw=i*i
        poz=kw
        while poz<=n:
            czyjest[poz-1]=1
            poz+=kw
    return czyjest
def liczba(n, k):
    l=sitko(n)
    return l[k]
print(sitko(100))