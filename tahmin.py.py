import random
 
sayi = random.randint(2, 18) #burdaki sayıya bilgisayar karar veriyor
tahmin = int(input("2 ile 18 arasında bir sayi tahmin et: "))

if tahmin == sayi:
    print("Tebrikler. Doğru tahmin!")
else: 
    print("Yanlış tahmin. Tekrar deneyiniz!")