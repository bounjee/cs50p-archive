def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    # format ile virgülden sonraki sadece 2 basamağı gösteriyoruz.
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # aldığımız değerdeki $ işaretini kaldırıyoruz.
    d = d.replace("$", "")
    # ifade yukarıda string olduğu için float'a çeviriyoruz
    d = float(d)
    # değeri döndürüyoruz dollars_to_float'yerine geliyor.
    return d


def percent_to_float(p):
    # aldığımız değerdeki % işaretini kaldırıyoruz.
    p = p.replace("%", "")
    # ifade yukarıda string olduğu için float'a çeviriyoruz
    p = float(p)
    # % ifadesinin tanımını yapıyoruz
    p = p / 100
    # değeri döndürüyoruz percent_to_float'yerine geliyor.
    return p


# main fonksiyonunu çağırıyoruz.
main()
