def cipher(key, txt0):
    size=len(key)
    n=len(key)
    zed =' '
    cyp= ' '
    for i in range(0,n,size):
        zed=[txt0[i+j] for j in range(size)]
        for j in range(size):
            cyp +=zed[key.index(j)]
    print (cyp)
    beggin()
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
        symbol(key,txt)
def symbol(key,txt):
    size=len(key)
    n=len(txt)
    if n%size !=0:
        for i in range (size-(n%size)):
            txt+=str(cipher(key,txt))
        print(cipher(key,txt))
def groups(key,txt):
    size=len(key)
    kolvo=int(input("Введите количество символов в группе: "))
    txt1=[txt[i:i+kolvo] for i in range(0,len(txt),kolvo)]
    if len(txt1[-1]) !=kolvo:
        for i in range(kolvo-(len(txt1[-1])%kolvo)):
            txt1[-1]+=str("/0")
    if len(txt)!=size:
        for i in range(size-(len(txt1)%size)):
            txt.append("/0"*kolvo)
    print(cipher(key,txt))
def beggin():
    print("Привет")
    print("Я умею шифровать сообщения")
    print("Выберите действие:")
    print("1 - зашифровать")
    print("2 - расшифровать")
    vib = int(input())
    if vib == 1:
        print("Вы выбрали действие 1,круто)")
    else:
        print("Действие два? Круто)")

beggin()

