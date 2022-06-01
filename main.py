def cipher(key, txt):
    size=len(key)
    n=len(key)
    zed = ' '
    cipher = ' '
    for i in range(0,n,size):
        zed=[txt[i+j] for j in range(size)]
        for j in range(size):
            cipher += zed[key.index(j)]
    return cipher

def symbol(key, txt):
    size=len(key)
    n=len(txt)
    if n % size != 0:
        for i in range(size-(n%size)):
            txt += str("/0")
    print(cipher(key, txt))
def groups(key, txt):
    size = len(key)
    poskolko = int(input("По сколько символов нужно группировать? "))
    text = [txt[i:i + poskolko] for i in range(0, len(txt), poskolko)]
    if len(text[-1]) != poskolko:
        for i in range(poskolko - (len(text[-1]) % poskolko)):
            text[-1] += str("/0")
    if len(text) != size:
        for i in range(size - (len(text) % size)):
            text.append("/0" * poskolko)
    print(cipher(key, text))
def word(key, txt):
    size = len(key)
    text = txt.split(" ")
    if len(text) != size:
        for i in range(size - (len(text) % size)):
            text.append("☭" * 5)
    k = len(text)
    block = ''
    code = ''
    for i in range(0, k, size):
        block = [text[i + j] for j in range(size)]
        for j in range(size):
            code += block[key.index(j)]
            code += " "
    print(code)
def choice():
    txt = input("Введите сообщение: ")
    print("Введите ключ шифрования, вводя цифры через пробел")
    print("Например, 3 1 0 2")
    k = input("Введите ключ\t")
    ke = k.split()
    key = []
    for e in ke:
        key.append(int(e))
    print("Выберите тип шифрования: ")
    print("1 - посимвольное")
    print("2 - группы")
    print("3 - слов ")
    kek = int(input())
    if kek == 1:
        symbol(key, txt)
    if kek == 2:
        groups(key, txt)
def beggin():
    print("Привет")
    print("Я умею шифровать сообщения")
    print("Выберите действие:")
    print("1 - зашифровать")
    print("2 - расшифровать")
    vib = int(input())
    if vib == 1:
        choice()
    else:
        print("Действие два? Круто)")
while(True):
    beggin()
    txt=0
