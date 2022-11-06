formats = input("Format? ")
formats = formats.casefold().strip()
# eğer formats .jpg veya diğer formatlarla bitiyorsa ona göre ekleme yapıyor.
# Örneğin a.jpg'yi image/jpeg atıyor
if formats.endswith(".jpg") or formats.endswith(".jpeg"):
    print("image/jpeg")
elif formats.endswith(".gif"):
    print("image/gif")
elif formats.endswith(".pdf"):
    print("application/pdf")
elif formats.endswith(".png"):
    print("image/png")
elif formats.endswith(".txt"):
    print("text/plain")
elif formats.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
