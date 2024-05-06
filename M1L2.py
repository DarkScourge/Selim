import random

sifre_secenekleri = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
soru = int(input("Şifrenizi uzunluğunu giriniz:"))
parola = ""
for i in range(soru):
    secenek = random.choice(sifre_secenekleri)
    parola+=secenek
print(parola)
