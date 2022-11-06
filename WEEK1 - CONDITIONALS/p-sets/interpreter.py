expression = input("Expression: ")
# expression'dan alınan ifadeyi x y z şeklinde yazmamızı bekliyor
x, y, z = expression.split(" ")

# üstte değerlerimiz string olduğu için alınacak değerleri float'a çeviriyoruz
new_x = float(x)
new_z = float(z)

# y'yi string olarak bırakıyoruz ve aşağıdaki işlemleri yapıyoruz
if y == "+":
    result = new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    result = new_x / new_z

print(result)
