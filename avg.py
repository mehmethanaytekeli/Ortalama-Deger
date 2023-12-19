import random
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
    if(kume[i]<100):
        kume1.append(kume[i])
    ortalama=toplam/100
print(kume1)
print(ortalama)