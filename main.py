def choice():
    txt=input("Введите сообщение: ")
    print("Введите ключ шифрования, вводя цифры через пробел")
    print("Например, 3 1 0 2")
    a=input("Введите ключ")
    ak=a.split()
    key=[]
    for i in ak:
        key.append(int(i))
    print("Выберите тип шифрования: ")
    print("1 - посимвольное")
    print("2 - группы")
    print("3 - слов \n")
    kek = int()
    if kek==1:
        simv(key,txt)
def simv(key,txt):
    size=len(key)
    n=len(txt)
    if n%size !=0:
        for i in range (size-(n%size)):
            txt+=str(cipher(key,txt))
        print(cipher(key,txt))
def cipher(key, txt):
    size=len(key)
    n=len(key)
    zed =' '
    cyp= ' '
    for i in range(0,n,size):
        zed=[txt[i+j] for j in range(size)]
        for j in range(size):
            cyp +=zed[key.index(j)]
    return cyp

print("Привет")
print("Я умею шифровать сообщения")
print("Выберите действие:")
print("1 - зашифровать")
print("2 - расшифровать")
vib = int()
if vib == 1:
    print("Вы выбрали действие 1,круто)")
else:
    print("Действие два? Круто)")

