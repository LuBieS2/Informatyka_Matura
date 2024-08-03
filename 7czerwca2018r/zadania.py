def loaddata(file):
    opn=open(file, "r")
    data=list(map(str.strip, opn.readlines()))
    data=[item.split(" ") for item in data]
    return data
def zadanie1():
    array1=loaddata("dane1.txt")
    array2=loaddata("dane2.txt")
    c=0
    for i in range(len(array1)):
        n=array1[i][len(array1[i])-1]
        m = array2[i][len(array2[i])-1]
        if n==m:
            c+=1
    print(c)
def zadanie2():
    global p2
    array1=loaddata("dane1.txt")
    array2=loaddata("dane2.txt")
    c=0
    for i in range(len(array1)):
         n1, n2, p1, p2 = 0, 0, 0, 0
         for n in array1[i]:
            n=int(n)
            if n%2==0:
                 p1+=1
            else:
                 n1+=1
         for n in array2[i]:
             n=int(n)
             if n%2==0:
                 p2+=1
             else:
                 n2+=1
         if n2 == n1 and p1==p2 and p1==5 and n2==5:
            c+=1
    print(c)
def zadanie3():
    array1=loaddata("dane1.txt")
    array2=loaddata("dane2.txt")
    it=[]
    c=0
    for i in range(len(array1)):
        k=set(array1[i])
        m=set(array2[i])
        if k==m:
            c+=1
            it.append(i+1)
    print(c, it)
def zadanie4():
    array1=loaddata("dane1.txt")
    array2=loaddata("dane2.txt")
    r=[]
    for i in range(len(array1)):
        temp=[]
        n1=0
        n2=0
        while n1<len(array1[i]) or n2<len(array2[i]):
            if len(array1[i])>n1 and len(array2[i])>n2:
                if int(array1[i][n1]) <= int(array2[i][n2]):
                    temp.append(array1[i][n1])
                    n1+=1
                else:
                    temp.append(array2[i][n2])
                    n2+=1
            else:
                if n1>n2:
                    temp.append(array2[i][n2])
                    n2+=1
                else:
                    temp.append(array1[i][n1])
                    n1+=1
        r.append(temp)
    for i in r:
        print(i, len(r))
zadanie4()