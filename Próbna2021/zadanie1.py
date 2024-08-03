def binary(a, k):
    A=[]
    for i in range(k):
        A.append(a%2)
        a=a//2
    A.reverse()
    return A
x=16
y=30
k=5
X=binary(x,k)
Y=binary(y,k)
round=k
for i in range(k):
    if X[i]==Y[i]:
        round-=1
    else:
        break
print(round)

