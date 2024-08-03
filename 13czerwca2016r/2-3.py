def nword(zbior):
    niggest_number=0
    for i in zbior:
        if i%2==0:
            if niggest_number%2==0 and niggest_number<i:
                niggest_number=i
        elif i%2==1:
            if niggest_number%2==0:
                niggest_number=i
            elif niggest_number>i:
                niggest_number=i
    return niggest_number

A=[1991,6,8,11,15,20,35,70,100,1000]
print(nword(A))