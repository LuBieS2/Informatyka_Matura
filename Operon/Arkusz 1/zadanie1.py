def loaddata(file):
    data=open(file, "r")
    array=list(map(str.strip, data.readlines()))
    return array
def isprime(a):
    if a==1:
        return False
    if a==2:
        return True
    for i in range(2, int(a**(1/2))+1):
        if a%i==0:
            return False
    return True
def lucky10000():
    k=1
    lucky1=[]
    lucky=[]
    for i in range(1, 10001):
        if i%2!=0:
            lucky.append(i)
    while k<len(lucky):
        for l, i in enumerate(lucky):
            n=int(lucky[k])
            if i!=n and (l+1)%n==0:
                lucky1.append(i)
        for i in lucky1:
            lucky.remove(i)
        k+=1
        lucky1=[]
    return lucky
def zadanie1():
    numbers=loaddata("dane.txt")
    lucky=[]
    c=0
    lucky=lucky10000()
    for i in numbers:
        i=int(i)
        if i in lucky:
            c+=1
    print(c)
def zadanie2():
    numbers = loaddata("dane.txt")
    lucky = []
    c = 0
    lucky=lucky10000()
    max=0
    max_i=0
    a=0
    c=0
    for i in numbers:
        i=int(i)
        if i in lucky:
            if c==0:
                a=i
            c+=1
        else:
            c=0
        if c>max:
            max=c
            max_i=a
    print(max, max_i)
def zadanie3():
    numbers=loaddata("dane.txt")
    lucky=lucky10000()
    c=0
    for i in numbers:
        i=int(i)
        if isprime(i) and i in lucky:
            c+=1
    print(c)
zadanie1()
zadanie2()
zadanie3()