n = int(input("Bir sayi gir: "))
faktoriyel = 1

for i in range(1, n+1):
    faktoriyel *= i

print(f"{n}! = {faktoriyel}")