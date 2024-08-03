def is_palindrom(number):
    number=str(number)
    if len(number)==1:
        return True
    reverse=""
    for i in range(len(number)):
        reverse+=number[len(number)-1-i]
    if reverse==number:
        return True
    return False
def new_palindrom(number, sym):
    number=str(number)
    reverse=""
    if sym:
        for i in range(len(number)):
            reverse+=number[len(number)-1-i]
    else:
        for i in range(len(number)):
            if i==0:
                pass
            else:
                reverse+=number[len(number)-1-i]
    palindrom=number+reverse
    return palindrom
def zadanie2():
    s=0
    for i in range(1, 1001):
        for k in range(2):
            p=new_palindrom(i, k)
            p=int(p)
            if p<1000000:
                b=str(bin(p)[2:])
                if is_palindrom(b):
                    s+=p
    print(s)
zadanie2()