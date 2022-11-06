def main():
    time = input("What time is it? ")
    c_time = convert(time)
    if c_time >= 7 and c_time <= 8:
        print("breakfast time")
    elif c_time >= 12 and  c_time <= 13:
        print("lunch time")
    elif c_time >= 18 and c_time <= 19:
        print("dinner time")





# zamanı string aldığımız için integer'e çevirip hesaplama yapıyoruz
def convert(time):
    # yazılan ifadeyi : ile ayırıyor. Örneğin 7:30'yi 5 ve 30 olarak ayırıyor
    hours, minutes = time.split(":")
    # 5 + (30/60) = 5 + 0.5 = 7.05 olarak çeviriyor ve breakfast time olarak main'e yazdırıyor
    hours = float(hours) + (float(minutes) / 60)
    return hours


# ana dosyamızın main olduğunu söylüyoruz.
if __name__ == "__main__":
    main()