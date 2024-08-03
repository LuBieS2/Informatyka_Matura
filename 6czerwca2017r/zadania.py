def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(int(number**(1/2))+1):
        if i==0 or i==1:
            pass
        elif number%i==0:
            return False
    return True

def loaddata(data):
    file=open(data, "r")
    lines=list(map(str.strip, file.readlines()))
    return lines
def zad1():
    array=loaddata("punkty.txt")
    array=[item.split(" ") for item in array]
    prime=[]
    for i in array:
        if is_prime(int(i[0])) and is_prime(int(i[1])):
            prime.append(i)
    print(len(prime))
zad1()
def zad2():
    array = loaddata("punkty.txt")
    array = [item.split(" ") for item in array]
    c=0
    for i in array:
        i[0]=set(i[0])
        i[1]=set(i[1])
    for i in array:
        if i[0]==i[1]:
            c+=1
    print(c)
zad2()
def zad3():
    array = loaddata("punkty.txt")
    array = [item.split(" ") for item in array]
    for i in array:
        i[0]=int(i[0])
        i[1]=int(i[1])
    niggest_range=0
    indexes=[]
    for n in array:
        for m in array:
            nm=((n[0]-m[0])**2+(n[1]-m[1])**2)**(1/2)
            if niggest_range<nm:
                niggest_range=nm
                indexes=[]
                indexes.append(m)
                indexes.append(n)
    print(niggest_range, indexes)
zad3()
def zad4():
    array = loaddata("punkty.txt")
    array = [item.split(" ") for item in array]
    for i in array:
        i[0]=int(i[0])
        i[1]=int(i[1])
    na_bokach=0
    w_srodku=0
    na_zewnatrz=0
    for n in array:
        if ((n[0]==5000 or n[0]==-5000) and (n[1]>=-5000 and n[1]<=5000)) or ((n[1]==5000 or n[1]==-5000) and (n[0]>=-5000 and n[0]<=5000)):
            na_bokach+=1
        if (n[0]>-5000 and n[0]<5000) and (n[1]>-5000 and n[1]<5000):
            w_srodku+=1
        if (n[0]<-5000 or n[0]>5000) or (n[1]<-5000 or n[1]>5000):
            na_zewnatrz+=1
    print(na_zewnatrz, na_bokach, w_srodku)
zad4()