def not_ekle(notlar, yeni_not):
    notlar.append(yeni_not)
    print("Not eklendi!")

def notlari_goster(notlar):
    if not notlar:
        print("Henüz not yok.")
    else:
        print("Notlar:")
        for i, n in enumerate(notlar,1):
            print(f"{i}. {n}")

def not_sil(notlar, index):
    if 0 < index <= len(notlar):
        silinen= notlar.pop(index-1)
        print(f"'{silinen}' silindi.") 
    else:
        print("Geçersiz seçim!")
        
notlar = []

while True:
    print("\n1- Not ekle\n2- Notları göster\n3- Not sil\n4- Çıkış")
    secim = input("Seçiminiz: ")

    if secim == "1":
        yeni_not = input("Yeni not gir: ")
        not_ekle(notlar, yeni_not)
    elif secim == "2":
        notlari_goster(notlar)
    elif secim == "3":
        notlari_goster(notlar)
        index = int(input("Silmek istediğiniz not numarası:"))
        not_sil(notlar, index)
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")