def luka(number1, number2):
    luka=(abs(int(number2)-int(number1)))
    return luka
def loaddata(file):
    data=open(file, "r")
    array=list(map(str.strip, data.readlines()))
    return array
def zadanie1():
    numbers=loaddata("dane4.txt")
    luki=[]
    for i in range(1,len(numbers)):
        luki.append(luka(numbers[i-1], numbers[i]))
    max=0
    min=abs(int(numbers[0])-int(numbers[1]))
    for i in luki:
        if i>max:
            max=i
        if i<min:
            min=i
    print(max, min)
def zadanie2():
    numbers=loaddata("dane4.txt")
    luka1=luka(numbers[0], numbers[1])
    c=2
    max=0
    first=numbers[0]
    mfirst=""
    mlast=""
    for i in range(2,   len(numbers)):
        if luka(numbers[i], numbers[i-1])==luka1:
            c+=1
        else:
            if c>max:
                max=c
                mfirst=first
                mlast=numbers[i-1]
            c=2
            first=numbers[i-1]
            luka1=luka(numbers[i], numbers[i-1])

    print(max, mfirst, mlast)
def zadanie3():
    numbers=loaddata("dane4.txt")
    luki=[]
    for i in range(1,len(numbers)):
        luki.append(luka(numbers[i-1], numbers[i]))
    sluki=[]
    slukin=[]
    for i in luki:
        if i not in sluki:
            sluki.append(i)
    for i in range(len(sluki)):
        slukin.append(0)
    for i in luki:
        k=sluki.index(i)
        slukin[k]+=1
    answer=[]
    maxs=0
    for i in slukin:
        if i>maxs:
            maxs=i
    for i in range(len(sluki)):
        if slukin[i]==maxs:
            answer.append([sluki[i], slukin[i]])
    print(answer)
zadanie3()