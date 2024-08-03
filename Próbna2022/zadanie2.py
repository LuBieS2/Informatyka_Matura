def czy_mozna(a, b):
    a=int(a)
    b=int(b)
    if a==1:
        return True
    while b!=a and b>=a:
        if b%2==0:
            b=b/2
        else:
            b=(b-1)/2
    if b==a:
        return True
    return False
def loaddata(file):
    data=open(file, "r")
    array=list(map(str.strip, data.readlines()))
    array=[item.split(" ") for item in array]
    return array
def zadanie():
    numbers=loaddata("pary.txt")
    c=0
    answer=[]
    for n in numbers:
        if czy_mozna(n[0], n[1]):
            c+=1
            answer.append([n[0], n[1]])
    print(answer, c)
zadanie()