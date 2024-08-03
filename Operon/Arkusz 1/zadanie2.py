def fibonacci(n):
    a1=1
    an=1
    if n==1 or n==2:
        return an
    for i in range(n-2):
        an, a1 = an+a1, an
    return an
tekst="NIEPRZYJACIELNADCHODZI"
szyfr=""
for k in range(1, len(tekst)+1):
    n=(fibonacci(k))%26
    szyfr+=(chr(65+(ord(tekst[k-1])-65+n)%26))
print(szyfr)
print(int("010010", 2))