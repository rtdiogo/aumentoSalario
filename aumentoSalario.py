

num1 = float(input('Insira o valor do seu salário: '))
aumento = 0

if(num1<=1045):
    print('Salário: R$ ', num1)
    aumento = num1 * 20 / 100
    print('Valor a acrescentar: R$ ', aumento)
    print('Novo salário: R$ ', num1 + aumento)
elif (num1 >= 1045.01 and num1 < 2015):
        print('Salário: R$ ', num1)
        aumento = num1 * 15 / 100
        print('Valor a acrescentar: R$ ', aumento)
        print('Novo salário: R$ ', num1 - aumento)
elif (num1 >= 2015.01 and num1 < 3250):
        print('Salário: R$ ', num1)
        aumento = num1 * 10 / 100
        print('Valor a acrescentar: R$ ', aumento)
        print('Novo salário: R$ ', num1 - aumento)
elif(num1>=3250.01):
    print('Salário: R$ ', num1)
    aumento = num1 * 5 / 100
    print('Valor a acrescentar: R$ ', aumento)
    print('Novo salário: R$ ', num1 - aumento)
