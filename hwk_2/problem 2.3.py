correct_symbols = ['+', '-', '*', '/', '0']
input_symbols = (input('Введите любой символ операции. Либо "0" для прекращения действий. '))
while input_symbols in correct_symbols:
    input_symbols = (input("Введите символ снова для операции: "))
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    if b == 0:
        print('На ноль делить низя')
    if input_symbols == '-':
        print(a-b)
    elif input_symbols == '+':
        print(a + b)
    elif input_symbols == '/':
        print(a / b)
    elif input_symbols == '*':
        print(a * b)
        input_symbols = (input("Введите символ снова для операции: "))
    if input_symbols == '0':
        print('Спасибо за тест')
        break
#Иногда калькулятор странно багуется и просит ввести символ снова. 
