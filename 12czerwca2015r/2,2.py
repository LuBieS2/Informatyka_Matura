c=[5, 15, 2,3,4,10,11,13,14,15,17,19,20,22,24]
n=len(c)
odp=[]
for i in c:
    if c[0]+c[1]>i and c[1]-c[0]<i:
        odp.append([c[0], c[1], i])
print(odp)