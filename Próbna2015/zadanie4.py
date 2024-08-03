def bubblesort(array):
    for j in array:
        for k in range(len(array)-1):
            if array[k] > array[k + 1]:
                array[k],  array[k+1]= array[k+1], array[k]
    return array
def numbertoarray(number):
    number=str(number)
    array=[]
    for i in number:
        array.append(int(i))
    return array
def loaddata(file):
    data=open(file, "r")
    array=list(map(str.strip, data.readlines()))
    array=[item.split(" ") for item in array]
    return array
def zadanieA():
    numbers=loaddata("dane_anagramy.txt")
    c=0
    for i in numbers:
        if len(i[0])!=len(i[1]):
            pass
        else:
            x=bubblesort(numbertoarray(i[0]))
            y=bubblesort(numbertoarray(i[1]))
            if x==y:
                c+=1
    print(c)
def zadanieB():
    numbers=loaddata("dane_anagramy.txt")
    numbers1=[]
    for i in numbers:
        numbers1.append(i[0])
        numbers1.append(i[1])
    sorted=[]
    for i in numbers1:
        sorted.append(bubblesort(numbertoarray(i)))
    print(sorted)
    ssorted=[]
    for i in sorted:
        if i not in ssorted:
            ssorted.append(i)
    count=[]
    for i in ssorted:
        count.append(0)
    for i in sorted:
        k=ssorted.index(i)
        count[k]+=1
    print(max(count))
zadanieA()
zadanieB()