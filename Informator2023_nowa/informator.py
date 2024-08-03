def loaddata(file):
    data=open(file, "r")
    array=list(map(str.strip, data.readlines()))
    return array
def z1_3():
    numbers=loaddata("dane1_3.txt")
    i=0
    m=0
    for n in numbers:
        t=[]
        t.append(numbers[i])

A=[1,2,3,4,5,6,7,8,9,10]
S=[]
for i in range(len(A)):
   S.append(A[i])
   for n in range(len(A)-i):
       S.append(A[n:n+i])
print(S)
