
a = int(input('podaj liczbe a'))
b = int(input('podaj liczbe b'))

if b<a:
    a,b=b,a

while b>=a:
    print(a,end=' ')
    a=a+1

