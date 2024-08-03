a=[1,1,4,4,4,2,1,5,5,2,1,0,1,1,1]
def progi(a):
    liczba_progów=0
    for i in range(1, len(a)):
        if a[i-1]>a[i]:
            liczba_progów+=1
    return liczba_progów
def proginajw(a):
    najw_liczba_progów=0
    c=0
    for i in range(1, len(a)):
        if a[i-1]>=a[i]:
            if a[i-1]>a[i]:
                c+=1
        else:
            if c>najw_liczba_progów:
                najw_liczba_progów=c
            c=0
    return najw_liczba_progów
print(proginajw(a))