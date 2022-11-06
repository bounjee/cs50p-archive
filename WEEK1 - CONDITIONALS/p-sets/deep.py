variable = input(
    "What is the Answer to Great Question of Life, the Universe and Everything? ")

# alınan değeri küçük harfe çevirip sağ ve solundaki boşlukları yok ediyoruz
variable = variable.casefold().strip()


if variable == "42" or variable == "forty two" or variable == "forty-two":
    print("Yes")
else:
    print("No")
