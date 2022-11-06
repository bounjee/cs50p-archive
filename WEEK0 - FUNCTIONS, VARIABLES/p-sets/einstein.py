# Kullanıcıdan değer alıyoruz
m = int(input("What's m variable : "))

# c'yi tanımlıyoruz
c = 300000000
# pow(deger,kare;küp)  pow fonksiyonu c'nin karesini alıyor 2->3 yaparsak küpünü alır.
c = pow(c, 2)

# E'yi tanımlıyoruz.
E = m * c

# değeri formatlayıp yazdırıyoruz
print(f"E: {E}")
