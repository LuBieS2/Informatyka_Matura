T=[1,1,2,2,3,3,4,4,5,5]
x=[]
y=[]
for i in T:
    if i not in x:
        x.append(i)
for i in x:
    y.append(0)
for i in T:
    k=x.index(i)
    y[k]+=1
max=0
for i in y:
    if i>max:
        max=i
moda=[]
for i in x:
    k=x.index(i)
    if y[k]==max:
        moda.append(i)
controlsum=0
for i in moda:
    controlsum+=max
if controlsum==len(T):
    moda=[]
print(moda)