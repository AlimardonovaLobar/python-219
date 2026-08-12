# variables - o'zgaruvchilar
num1 = 10 
num2 = 20

# Data types - malumot turlari
# int, float, bool, string

# int - butun son - 10, 20, 11, 30
# float - kasr son - 11.2, 22.3 va hokozo
# str - matn - "hello", 'world' -> pep8
# bool - mantiqiy - True, False

# print funksiya - qiymatni chop etishga ishlatamiz - print("Lobar") -> result: Lobar

# o'zgaruvchilarni nomalashdagi qoidalar:
# 3 ta metod bor
# 1. snake_case - variable, function
# 2. PascalCase - Klass
# 3. camelCase - js

first_name = "hello lobar"
last_name = "alimardonova"
age = 16
occupation = "student"

# 1-way
print(f"This is {first_name} {last_name}. She is {age} years old and a {occupation}.") # -> "This is Alimardonova Lobar. She is 16 years old and a student."
# 2-way
print("This is " + first_name + " " + last_name + ". She is " + str(age) + " years old and a " + occupation + ".")
# 3-way
print("This is %s %s. She is %d years old and a %s." % (first_name, last_name, age, occupation))
# 4-way
print("This is {} {}. She is {} years old and a {}.".format(first_name, last_name, age, occupation))
# static vs dynamic
# static - o'zgarmas data
# dynamic - o'zgaruvcha data

# casting - bitta malumot turidan boshqa bir malumot turiga o'tkazish str(age)

# metod bu - string ustida har xil amal bajarib beradigan vosita
# doim metodni chaqirish uchun obyektdan keyin nuqta orqali metod nomi va qavs qoyiladi
print(first_name.title()) # uchragan so'zni bosh harfini katta qilib beradi
print(first_name.capitalize()) # butun mattni bosh harfini katta qilib beradi
print(first_name.lower()) # hammasini kichik qilib beradi
print(first_name.upper()) # hammasini katta qilib ber
print(first_name.replace("lobar", "Abdulla")) 

# raqamlar ustida arifmetik amallar
num1 = 10
num2 = 5
print(num1 + num2) # 15
print(num1 - num2) # 5
print(num1 * num2) # 50
print(num1 / num2) # 2.0
print(num1 // num2) # 2
print(num1 % num2) # 0

print(f"{num1} va {num2} larning yi'gindisi {num1 + num2} ga teng.")


age = int(input("Tug'ilgan yilingizni kiriting>>>>"))

print(f"Siz {2026 - age} yoshda ekansiz.")