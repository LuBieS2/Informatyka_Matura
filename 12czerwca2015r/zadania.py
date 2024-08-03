def loaddata(file):
    data=open(file, "r")
    array=list(map(str.strip, data.readlines()))
    return array
def code(number):
    l=loaddata("cyfra_kodkreskowy.txt")
    l=l[1:]
    control=controlnumber(number)
    l=[item[2:] for item in l]
    c=[]
    c.append("11011010")
    for i in range(len(number)):
        n=int(number[i])
        c.append(l[n])
    c.append(l[control])
    c.append("11010110")
    return c
def controlnumber(number):
    p=[]
    n=[]
    for i in range(len(number)):
        if i%2!=0:
            p.append(int(number[i]))
        else:
            n.append(int(number[i]))
    ps=0
    ns=0
    for i in p:
        ps+=i
    ps=ps*3
    for i in n:
        ns+=i
    ps+=ns
    ps=ps%10
    ps=10-ps
    ps=ps%10
    return ps
def zadanie1():
    numbers=loaddata("kody.txt")

    for number in numbers:
        p=[]
        n=[]
        for i in range(len(number)):
            if i%2!=0:
                p.append(int(number[i]))
            else:
                n.append(int(number[i]))
        ps=0
        ns=0
        for i in p:
            ps+=i
        for i in n:
            ns+=i
        print(ps, ns)
def zadanie2():
    numbers=loaddata("kody.txt")
    l=loaddata("cyfra_kodkreskowy.txt")
    l=l[1:]
    l=[item[2:] for item in l]
    for number in numbers:
        coded=code(number)
        cc=coded[-2]
        n=l.index(cc)
        print(n, cc)
def zadanie3():
    numbers=loaddata("kody.txt")
    for number in numbers:
        print(code(number))
zadanie3()