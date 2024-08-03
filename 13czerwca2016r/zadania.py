def loaddata(file):
    data=open(file, "r")
    array=list(map(str.strip, data.readlines()))
    return array
def zad1():
    numbers=loaddata("liczby.txt")
    c=0
    for i in numbers:
        if i[-1]=="8":
            c+=1
    print(c)
zad1()
def zad2():
    numbers=loaddata("liczby.txt")
    fours=[]
    answer=0
    for i in numbers:
        if i[-1]=="4":
            fours.append(i[:len(i)-1])
    for number in fours:
        n=0
        for digit in number:
            if digit=="0":
                n+=1
        if n==0:
            answer+=1
    print(answer)
zad2()
def zad3():
    numbers = loaddata("liczby.txt")
    twos=[]
    for i in numbers:
        if i[-1] == "2":
            twos.append(int(i[:len(i) - 1], 2))
    c=0
    for i in twos:
        if i%2==0:
            c+=1
    print(c)
zad3()
def zad4():
    numbers = loaddata("liczby.txt")
    eights=[]
    for i in numbers:
        if i[-1] == "8":
            eights.append(int(i[:len(i) - 1], 8))
    s=0
    for i in eights:
        s+=i
    print(s)
zad4()
def zad5():
    numbers = loaddata("liczby.txt")
    n10=[]
    for i in numbers:
        n=int(i[-1])
        n10.append(int(i[:len(i) - 1], n))
    smallest_number=n10[0]
    s_index=0
    biggest_number=0
    b_index=0
    for n, i in enumerate(n10):
        if i>biggest_number:
            biggest_number=i
            b_index=n
        if i<smallest_number:
            smallest_number=i
            s_index=n
    print(biggest_number, numbers[b_index], smallest_number, numbers[s_index])
zad5()