import random
b=0
while 1:
    a=100
    toplam=0
    ortalama=0
    kume =[]
    kume1=[]
    while(a>0):
        sayi=int(random.randint(0, 1000))
        kume.append(sayi)
        a =a-1
    for i in range(0,100,1):
        toplam +=kume[i]
        ortalama=toplam/100
    print(ortalama)
    if(ortalama==500):
        print(b,"Deneme",ortalama)
        break
    else:
        b =b+1

