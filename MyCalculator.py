def basicCalculator(myoper, myvar1, myvar2):
    if (myoper == '1'):
        myvar3 = int(myvar1) + int(myvar2)
        print("%d + %d = %d" % (int(myvar1), int(myvar2), myvar3))
    elif (myoper == '2'):
        myvar3 = int(myvar1) - int(myvar2)
        print("%d - %d = %d" % (int(myvar1), int(myvar2), myvar3))
    elif (myoper == '3'):
        myvar3 = int(myvar1) * int(myvar2)
        print("%d * %d = %d" % (int(myvar1), int(myvar2), myvar3))
    elif (myoper == '4'):
        myvar3 = int(myvar1) / int(myvar2)
        print("%d / %d = %d" % (int(myvar1), int(myvar2), myvar3))


print('Selecione o número da operação desejada\n'
      '1 - soma\n'
      '2 - subtração\n'
      '3 - multiplicação\n'
      '4 - divisão\n')

myOper = input('Digite sua opção (1/2/3/4/5): ')

myVar1 = input('Digite o primeiro número: ')
myVar2 = input('Digite o segundo número: ')

basicCalculator(myOper, myVar1, myVar2)
