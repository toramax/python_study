# = равно
# == соответствует
# >= больше равно
# <= меньше равно
# != неравно


# Мой калькулятор №1

num1 = float( input("Число 1: ") )
what = input( "Введите операцию (+, -, *, /): " )
num2 = float( input("Число 2: ") )

if what == "+":
    res = num1+num2
    print ("Результат: " + str (res) )
if what == "-":
    res = num1-num2
    print ("Результат: " + str (res) )
if what == "*":
    res = num1*num2
    print ("Результат: " + str (round (res) ) )
if what == "/":
    res = num1/num2
    print ("Результат: " + str (round (res) ) )