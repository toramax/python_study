 # Типы данных:
#int (integer )
#number = 5
#Float
#snumber = 5.7
#str
#myname = "MaxS"
#bool (буливо значение)
#status = True
#Функция вывода: print
#print ("Что нужно вывести на экран")
#Экранирование \
#print ("Что нужно \"вывести\" на экран")
#print ('Что нужно "вывести" на экран')

#Перенос строки
#print ("Что нужно \nвывести на экран")

#Конкатенация
#print ("Нужно " + myname + " вывести на экран")

#print ("Ему " + str(snumber) + " лет")

#name = input( "Введите свое имя: " )
#age = input( "Укажите свой возраст: " )

#Вывод на экран
#print ("Привет " + name + " !")
#print ("Тебе уже " + age + " год,\nты красавчик!!! =))")


# Математика: +, -, *, /, **-степень, %-деление по модулю, унарный минус, округление, Пи
#a = 5
#b = 10

#c = a + b
#print( c )
#import math
#print( math.pi )

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