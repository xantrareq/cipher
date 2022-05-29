def cipher(key, text):
    size=len(key)
    n=len(key)
    block =' '
    code= ' '
    for i in range(0,n,size):
        block=[text[i+j] for j in range(size)]
        for j in range(size):
            code +=block[key.index(j)]
    return code

print("Привет")
print("Я умею шифровать сообщения")
print("Привет")
print("Выберите действие:")
print("1 - зашифровать")
print("2 - расшифровать")
vib = int()
if vib == 1:
    print("Вы выбрали действие 1,круто)")
else:
    print("Действие два? Круто)")
    print("zzzz")
