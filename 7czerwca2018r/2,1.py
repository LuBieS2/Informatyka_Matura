def sq(n):
    return n*n
def F(n):
    f1=1
    f2=1
    if n==1 or n==2:
        return 1
    for i in range(n-2):
        x=f2
        f2=f1+f2
        f1=x
    return f2
print(F(7))
def F1(n):
    if n==1 or n==2:
        return 1
    else:
        if n%2==0:
            k=n/2
            return sq(F1(k+1))-sq(F1(k-1))
        else:
            k=n//2+1
            return sq(F1(k))+sq(F1(k-1))
print(F1(7))