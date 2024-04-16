

#variant 17
#0,1,0,1,0,1,0,1
m = 7
j = 0
zero = 0
one = 0
chet = 0
nechet = 0
register = [0,1,0,1,0,1,0,1]
startRegisterForSverka = [0,1,0,1,0,1,0,1]
arrayforFunc = [1,1,1,0,0,0,0,1,1] #коэффициенты многочлена F(x)
print('начальное состояние регистра = ', register)
flag = True
print(flag)


def bigSumma (register,arrayforFunc):
    #print('registe arrive = ', register)0110100
   # print('F(x)=', arrayforFunc)

    const = arrayforFunc[0]
    #print('CONST = ', const)
    
    i = 0
    summa = 0
    while (i<8):
        
        summa = summa ^ arrayforFunc[i+1]*register[i]
        i = i + 1
   # print('summa and const = ', summa + const)
    return (summa ^ const)

myGamma = []


iterator = 0

while (flag):

    lastelem = bigSumma(register, arrayforFunc)
    elemGamma = register[j]
    if elemGamma%2 == 0:
        zero = zero + 1
    else:
        one = one + 1
    myGamma.append(elemGamma)
    
    while (j < 8):
        
        if (j+1 != 8):
            
            elemGamma = register[j]
            register[j] = register[j+1]
            
            j = j + 1
        else:
            elemGamma = register[j]
            register[j] = lastelem%2
            
            j = j + 1
    j = 0
    iterator = iterator + 1    
    if (startRegisterForSverka == register):
        flag = False
    print('sostoyanie regista ITRATION ', iterator , ' = ',  register)
    #print('sostoyanie gamma ITRATION ', iterator , ' = ',  myGamma)
period = len(myGamma)

print('zero = ', zero)
print('one = ', one)
print('period = ', period)
print('iterator = ', iterator)
print('end register',register)
print('end gamma = ', myGamma)
print('тип начальной гаммы = ', type(myGamma))
print('начинаю преобразовыввать гамму')
    
array_bit = [] 
for i in range(0, len(myGamma), 8):
    array_bit.append(myGamma[i:i+8])

print('после 1ого шага = ', array_bit)
i = 0
strArrayBit = str(array_bit)

strArrayBit = strArrayBit.replace(',', '')
strArrayBit = strArrayBit.replace('[', '')
strArrayBit = strArrayBit.replace(']', '')
strArrayBit = strArrayBit.replace(' ', '')

print('после перевода в стр и удаления символов')
print('после 2 ого шага = ', strArrayBit)
print('предположительно строка битов = ', type(strArrayBit))


newBitArray = []
newByteArray = []
for i in range(0, len(strArrayBit), 8):
    newBitArray.append(strArrayBit[i:i+8])
print('третье преобразование строки битов')
print('bitArray = ', newBitArray)

for i in range(0, len(newBitArray)):
    newByteArray.append(int(newBitArray[i],2))
print('newByteArray = ',newByteArray)
i = 0
while (i<len(newByteArray)):
    if (newByteArray[i]%2==0):
        chet = chet + 1
    else:
        nechet = nechet + 1
    i = i + 1


print('chet = ', chet)

print('nechet = ', nechet)
i = 0
#тут начинается шифр гаммирования (lab 3)
file = "text.txt"
file1 = "1.txt"
file2 = "lab3.odt"

file3 = "lab3.pdf"
file4 = "1.png"

def encrypt_file(file):  # метод шифрования
    with open(file, 'rb') as f:
        file_code = f.read()  # чтение файла побитово

    file_code = "".join(format(c, '08b') for c in file_code)  # перевод десятичных значений в двоичные, где один символ кодируется 8-ю битами
    i = 0
    
    newGammaForFileCode = []# отрезаю часть гаммы по длине сообщения
    print ('i= ', i)
    print("my gamma TEST == ", myGamma)
    while i < len(file_code):
        print('str 137: i = ', i)
        newGammaForFileCode.append(myGamma[i])
        
        i = i + 1
    print("newGammaForFileCode= ", newGammaForFileCode)
    print('')
    print('00000000 file code = ',file_code)
    newGammaForFileCode = str(newGammaForFileCode)

    newGammaForFileCode = newGammaForFileCode.replace(',', '')
    newGammaForFileCode = newGammaForFileCode.replace('[', '')
    newGammaForFileCode = newGammaForFileCode.replace(']', '')
    newGammaForFileCode = newGammaForFileCode.replace(' ', '')

    
    
    print("newGammaForFileCode= ", newGammaForFileCode)

    print ("длина отрезанной гаммы = ", len(newGammaForFileCode))
    print ("длина файла с сообщением = ", len(file_code))

    #ксорим получаем шифр текст
    shtext = []
    i =0
    while (i<len(file_code)):
        print("check LOGIC RES = ", (file_code[i] == newGammaForFileCode[i]))
        if (file_code[i] == newGammaForFileCode[i]):
            
            print("i = ", i)
            shtext.append(0)
        else:
            print("i = ", i)
            shtext.append(1)
        i= i + 1

    print("shtext = ", shtext)
    #преобразуем шифрт текст в строку без лишних символов
    shtext = str(shtext)
    shtext = shtext.replace(',', '')
    shtext = shtext.replace('[', '')
    shtext = shtext.replace(']', '')
    shtext = shtext.replace(' ', '')
    print("newGammaForFileCode= ", newGammaForFileCode)
    print('00000000 file code = ',file_code)
    print("00000000 strShText = ", shtext)
    print('тип шифротекста = ', type(shtext))

    shtextBitArrayBlock = []
    shtextByteArray = []
    for i in range(0, len(shtext), 8):
        shtextBitArrayBlock.append(shtext[i:i+8])
    print('Block bit sh text = ', shtextBitArrayBlock)

    for i in range(0, len(shtextBitArrayBlock)):
        shtextByteArray.append(int(shtextBitArrayBlock[i],2))
    print('БАЙТЫ ШИФРОТЕКСТА', shtextByteArray)


    
    #шифрование файла
    

    
    with open(file, 'wb') as f:
        f.write(bytes(shtextByteArray))  # запись масива в файл

    print(f"Файл {file} зашифрован.")


encrypt_file(file2)


