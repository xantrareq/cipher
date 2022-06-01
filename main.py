def cipher(key, txt):
    size = len(key)
    z = len(txt)
    zed = ''
    cip = ''
    for i in range(0, z, size):
        zed = [txt[i + j] for j in range(size)]
        for j in range(size):
            cip += zed[key.index(j)]
    return cip


def symbol(key, txt):
    size = len(key)
    z = len(txt)
    if z % size != 0:
        for i in range(size - (z % size)):
            txt += str("★")
    print(cipher(key, txt))


def groups(key, txt):
    size = len(key)
    kolvo = int(input("Сколько символов сгруппировать? "))
    text = [txt[i:i + kolvo] for i in range(0, len(txt), kolvo)]
    if len(text[-1]) != kolvo:
        for i in range(kolvo - (len(text[-1]) % kolvo)):
            text[-1] += str("★")
    if len(text) != size:
        for i in range(size - (len(text) % size)):
            text.append("★" * kolvo)
    print(cipher(key, text))

def word(key, txt):
    size = len(key)
    text = txt.split(" ")
    if len(text) != size:
        for i in range(size - (len(text) % size)):
            text.append("★"*3)
    z = len(text)
    zed = ''
    cyp = ''
    for i in range(0, z, size):
        zed = [text[i + j] for j in range(size)]
        for j in range(size):
            cyp += zed[key.index(j)]
            cyp += " "
    print(cyp)

def choice():
    txt = input("Введите сообщение: ")
    print("Введите ключ шифрования, вводя цифры через пробел")
    print("Например, 3 1 0 2")
    k = input("Ключ:\t ")
    ke = k.split()
    key = []
    for e in ke:
        key.append(int(e))
    print("Выберите тип шифрования: ")
    print("1 - посимвольное")
    print("2 - группы")
    print("3 - слов ")
    kek = int(input("Ваш выбор: "))
    if kek == 1:
        symbol(key, txt)
    if kek == 2:
        groups(key, txt)
    if kek == 3:
        word(key, txt)

def decip(key, txt):
    size = len(key)
    z = len(txt)
    zed = ''
    cyp = ''
    for i in range(0, z, size):
        zed = [txt[i + j] for j in range(size)]
        for j in range(size):
            cyp += zed[key[j]]
    cyp = cyp.replace("★", "")
    return cyp
def desymbol(key, txt):
    print(decip(key, txt))

def degroups(key, txt):
    kolvo = int(input("Сколько символов сгруппировать? "))
    text = [txt[i:i + kolvo] for i in range(0, len(txt), kolvo)]
    print(decip(key, text))

def deword(key, txt):
    text = txt.split(" ")
    size = len(key)
    n = len(text)
    zed = ''
    cipher = ''
    if len(text) != size:
        for i in range(size - (len(text) % size)):
            text.append("★")
    z = len(text)
    for i in range(0, n, size):
        zed = [text[i + j] for j in range(size)]
        for j in range(size):
            cipher += zed[key[j]]
            cipher += " "
    cipher = cipher.replace("★", "")
    print(cipher)


def dechoice():
    txt = input("Введите сообщение: ")
    print("Введите ключ шифрования, вводя цифры через пробел")
    print("Например, 3 1 0 2")
    k = input("Ключ: \t")
    ke = k.split()
    key = []
    for e in ke:
        key.append(int(e))
    print("Выберите тип шифрования: ")
    print("1 - посимвольное")
    print("2 - группы")
    print("3 - слов ")
    kek = int(input("Ваш выбор"))
    if kek == 1:
        desymbol(key, txt)
    if kek == 2:
        degroups(key, txt)
    if kek == 3:
        deword(key, txt)

def beggin():
    print("Привет")
    print("Я умею шифровать сообщения")
    print("Выберите действие:")
    print("1 - зашифровать")
    print("2 - расшифровать")
    vib = int(input("Ваш выбор: "))
    if vib == 1:
        choice()
    if vib == 2:
        dechoice()



while(True):
    beggin()
    txt=0