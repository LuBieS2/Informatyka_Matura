def loaddata():
    file=open("C:\\Users\\jonas\\Desktop\\Informatyka Matura\\Informator2023_nowa\\dane1_3.txt", "r")
    C=list(map(str.strip, file.readlines()))
    return C
A=[1,2,3,4,5,67,8,3,12,5,43]
def getsequences(array):
    n=len(array)
    All_sequnces=[]
    for i in range(1,n+1):
        sequences=n-i+1
        for j in range(sequences):
            All_sequnces.append(array[j:j+i])
    return All_sequnces
getsequences(A)
def getsequnces_len(array):
    n=len(array)
    return int(((n+1)/2)*n)
print(len(getsequences(A)), getsequnces_len(A))