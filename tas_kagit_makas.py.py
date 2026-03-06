import random

print("Taş-Kağıt-Makas Oyununa Hoşgeldiniz!")

secenekler = ["taş", "kağıt", "makas"]

while True:
    oyuncu = input("Seçiminizi yapın(taş/kağıt/makas): ").lower() #yazdığımız tüm harfleri küçük harflere dönüştürür lower
    if oyuncu not in secenekler:
        print("Geçersiz seçim, tekrar deneyin.")
        continue 

    bilgisayar =random.choice(secenekler)
    print("Bilgisayarın seçimi:", bilgisayar)

    if oyuncu == bilgisayar:
        print("Berabere!")
    elif (oyuncu == "taş" and bilgisayar == "makas") or \
         (oyuncu == " kağıt" and bilgisayar == "taş") or\
         (oyuncu == "makas" and bilgisayar==" kağıt"):
        print("Kazandınız")
    else:
        print("Kaybettiniz:")

    tekrar =input ("Tekrar oynamak ister misiniz?  (evet/hayır):").lower()
    if tekrar != "evet":
        print("Oyun bitti, teşekkürler!")
        break 
