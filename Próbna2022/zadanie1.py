def loaddata(file):
    data=open(file, "r")
    array=list(map(str.strip, data.readlines()))
    array=array[0]
    return array
def zadanie1():
    match=loaddata("mecz.txt")
    c=0
    for i in range(len(match)-1):
        if match[i+1]!=match[i]:
            print(match[i], match[i+1])
            c+=1
    print(c)
def zadanie2():
    match=loaddata("mecz.txt")
    A=0
    B=0
    winner=""
    for i in match:
        if A>=1000 and A-B>=3:
            winner="A"
            break
        if B>=1000 and B-A>=3:
            winner="B"
            break
        if i=="A":
            A+=1
        if i=="B":
            B+=1
    print(winner, A,":",B)
def zadanie3():
    match=loaddata("mecz.txt")
    cp=0
    widest=0
    widest_n=""
    p = match[0]
    c = 1
    for i in range(1, len(match)):
        if p==match[i]:
            p=match[i]
            c+=1
        else:
            if c>=10:
                cp+=1
                if c>widest:
                    widest=c
                    widest_n=p
            p=match[i]
            c=1
    print(widest, widest_n, cp)
