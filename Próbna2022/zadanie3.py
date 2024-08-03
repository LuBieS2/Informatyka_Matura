def loaddata(file):
    data=open(file, "r")
    array=list(map(str.strip, data.readlines()))
    return array
def is_prime(a):
    if a==1:
        return False
    if a==2:
        return True
    for i in range(2, int(a**(1/2))+1):
        if a%i==0:
            return False
    return True
def goldbach(a):
    a=int(a)
    c=0
    for i in range(int(a/2)+1):
        if is_prime(i):
            n=a-i
            if is_prime(n):
                c+=1
    return c
def zadanie1():
    numbers=loaddata("liczby.txt")
    c=0
    for i in numbers:
        n=int(i)-1
        if is_prime(n):
            c+=1
    print(c)
def zadanie2():
    numbers=loaddata("liczby.txt")
    min=goldbach(numbers[0])
    min_i=numbers[0]
    max=0
    max_i=0
    for i in numbers:
        i=int(i)
        n=goldbach(i)
        if n>max:
            max=n
            max_i=i
        if n<min:
            min=n
            min_i=i
    print(max, max_i, min, min_i)
def zadanie3():
    numbers=loaddata("liczby.txt")
    c0=0
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    c7=0
    c8=0
    c9=0
    A=0
    B=0
    C=0
    D=0
    E=0
    F=0
    for i in numbers:
        i=int(i)
        n=hex(i)[2:]
        for x in n:
            if x=="0":
                c0+=1
            if x=="1":
                c1+=1
            if x=="2":
                c2+=1
            if x=="3":
                c3+=1
            if x=="4":
                c4+=1
            if x=="5":
                c5+=1
            if x=="6":
                c6+=1
            if x=="7":
                c7+=1
            if x=="8":
                c8+=1
            if x=="9":
                c9+=1
            if x=="a":
                A+=1
            if x=="b":
                B+=1
            if x=="c":
                C+=1
            if x=="d":
                D+=1
            if x=="e":
                E+=1
            if x=="f":
                F+=1
    print("0", c0)
    print("1", c1)
    print("2", c2)
    print("3", c3)
    print("4", c4)
    print("5", c5)
    print("6", c6)
    print("7", c7)
    print("8", c8)
    print("9", c9)
    print("A", A)
    print("B", B)
    print("C", C)
    print("D", D)
    print("E", E)
    print("F", F)