# = равно
# == соответствует
# >= больше равно
# <= меньше равно
# != неравно

if 1:
    print ("True")
    print ("All is ok")
# При значении 0, проверка функции не произойдет и значение не выведутся.
if 0:
    print ("False")
    print ("Error. Check log file")
print("All is cool!")

num = input ("Введите ваше имя: ")
if num == "Max":
    print ("hello Max! Welcome to pythoncode")
elif num == "v":
    print ("V means Vendetta\nWelcome Guy Fawkes ")

else:
    print ("Alejandro")


#A = "Hello.\nThank you for collaboration" if num != "Test" else "Congratulations! At last we have found you!"
#print (A)