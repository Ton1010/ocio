n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

a = 0
sig = ""
print("Suma de los divisrores de:",n1,"=",end=" ")

for i in range(1,n1+1):
    if n1%i==0:
        h = i
        if h!=n1:
            print(h,end="")
            if h==n1:
                print(end="")
            else:
                print("+",end="")
        c = h+a
        a = c
l = c-n1
print("=",l)
print()


w = 0
print("Suma de los divisrores de:",n2,"=",end=" ")
for u in range(1,n2+1):
    if n2%u==0:
        o = u
        if o!=n2:
            print(o,end="+",)
        s = o+w
        w = s
f = s-n2
print("=",f)


if l==n2:
    if f==n1:
        print("Los dos numeros son amigos.")
    else:
        print("Los numeros se odian, NO SON AMIGOS")
else:
    print("Ni se conocen, NO SON AMIGOS")
