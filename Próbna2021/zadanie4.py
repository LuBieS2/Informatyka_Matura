def loaddata(file):
    data=open(file, "r")
    array=list(map(str.strip, data.readlines()))
    return array
print(loaddata("galerie_przyklad.txt"))
def zadanie1():
    galerie=loaddata("galerie.txt")
    countries=[]
    for i in galerie:
        x=""
        for n in i:
            if n!=" ":
                x+=n
            else:
                break
        countries.append(x)
    countries=list(set(countries))
    counter=[]
    for i in countries:
        counter.append(0)
    for i in galerie:
        x=""
        for l in i:
            if l != " ":
                x += l
            else:
                break
        k=countries.index(x)
        counter[k]+=1
    for i in range(len(countries)):
        print(countries[i], counter[i])
def zadanie2():
    galerie=loaddata("galerie.txt")
    galerie=[item.split(" ") for item in galerie]
    c=0
    wymiary=[]
    max=0
    max_i=""
    p1=0
    for n, i in enumerate(galerie[0]):
        p=0
        if n>1 and n%2==0:
            p=int(galerie[0][n])*int(galerie[0][n+1])
        p1+=p
    min=p1
    min_i=galerie[0][1]
    for i in galerie:
        cg=0
        pg=0
        for n, k in enumerate(i):
            p = 0
            if n > 1 and n % 2 == 0:
                p = int(i[n]) * int(i[n + 1])
                if p>0:
                    cg+=1
            pg+=p
        if pg>max:
            max=pg
            max_i=i[1]
        if pg<min:
            min=pg
            min_i=i[1]
        wymiary.append([i[1], pg, cg])
    print(wymiary)
    print(min_i, min)
    print(max_i, max)
def zadanie3():
    galerie=loaddata("galerie.txt")
    galerie=[item.split(" ") for item in galerie]
    max=0
    max_i=""
    rooms1=[]
    for n, k in enumerate(galerie[0]):
        p = 0
        if n > 1 and n % 2 == 0:
            p = int(galerie[0][n]) * int(galerie[0][n + 1])
            if p != 0:
                rooms1.append(p)
    rooms1len=len(set(rooms1))
    min=rooms1len
    min_i=galerie[0][1]
    for i in galerie:
        rooms=[]
        for n, k in enumerate(i):
            p = 0
            if n > 1 and n % 2 == 0:
                p = int(i[n]) * int(i[n + 1])
                if p!=0:
                    rooms.append(p)
        roomsnum=len(set(rooms))
        if roomsnum>max:
            max=roomsnum
            max_i=i[1]
        if roomsnum<min:
            min=roomsnum
            min_i=i[1]
    print(max_i, max)
    print(min_i, min)
zadanie3()