def cipher(key, txt):
    size=len(key)
    n=len(key)
    zed = ' '
    cyp = ' '
    for i in range(0,n,size):
        zed=[txt[i+j] for j in range(size)]
        for j in range(size):
            cyp += zed[key.index(j)]
    return cyp

def symbol(key, txt):
    size=len(key)
    n=len(txt)
    if n % size != 0:
        for i in range(size-(n%size)):
            txt += str("/0")
    print(cipher(key, txt))
def groups(key, txt):
    size = len(key)
    kolvo = int(input("По сколько символов нужно группировать? "))
    text = [txt[i:i + kolvo] for i in range(0, len(txt), kolvo)]
    if len(text[-1]) != kolvo:
        for i in range(kolvo - (len(text[-1]) % kolvo)):
            text[-1] += str("/0")
    if len(text) != size:
        for i in range(size - (len(text) % size)):
            text.append("/0" * kolvo)
    print(cipher(key, text))
def word(key, txt):
    size = len(key)
    text = txt.split(" ")
    if len(text) != size:
        for i in range(size - (len(text) % size)):
            text.append("/0" * 5)
    k = len(text)
    block = ''
    cyp = ''
    for i in range(0, k, size):
        block = [text[i + j] for j in range(size)]
        for j in range(size):
            cyp += block[key.index(j)]
            cyp += " "
    print(cyp)

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
    if kek == 3:
        word(key, txt)
def decip(key, txt):
    size = len(key)
    n = len(txt)
    block = ''
    cyp = ''
    for i in range(0, n, size):
        block = [txt[i + j] for j in range(size)]
        for j in range(size):
            cyp += block[key.index(j)]
    cyp = cyp.replace("/0", "")
    return cyp
def desymbol(key, txt):
    for i in range(len(key) // 2):
        key[i], key[-i - 1] = key[-i - 1], key[i]
    print(decip(key, txt))
def beggin():
    print("Привет")
    print("Я умею шифровать сообщения")
    print("Выберите действие:")
    print("1 - зашифровать")
    print("2 - расшифровать")
    vib = int(input("Ваш выбор: "))
    if vib == 1:
        choice()
    else:
        print("Ладно")

while(True):
    beggin()
    txt=0