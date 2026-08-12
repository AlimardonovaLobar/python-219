#sinf ishi:
#method, loop, if, random


#10-masala:
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))


# if a<b<c or c<b<a:
#     print("b soni a va c sonlari o'rtasida.")
# else:
#     print("b soni o'rtasida emas.")
#---------------------------------------------------




#11-masala:
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))

# count=0
# if a>0: 
#     count+=1
# if b>0:
#     count+=1
# if c>0:
#     count+=1

# print(count)
#---------------------------------------------------





#12-masala:
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))

# count = a+b+c
# if a<b  and a<c:
#     print(count-a)
# elif b<a and b<c:
#     print(count-b)
# else:
#     print(count-c)
#---------------------------------------------------------------------





#13-masala:
# a = int(input("Birinchi sonni kiriting: "))

# i = 1
# count = 0
# while a<i:
#     if a%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("tub son")






#14-misol:
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))



# if a%2==1 and b%2==1:
#     print("a va b soni toq son")
# elif a%2==1:
#     print("a soni toq son")
# elif b%2==1:
#     print(" b soni toq son")
# else:
#     print("ikkala son ham juft son")
#----------------------------------------------------



#14-masala:
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))


# if a%2==1 and b%2==1:
#     print("a va b soni toq son")
# elif a%2==1:
#     print("a soni toq son")
# elif b%2==1:
#     print(" b soni toq son")
# else:
#     print("ikkala son ham juft son")
#--------------------------------------------------




#16-masala:


# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))


# if a>0 and b>0:
#     print("a va b soni musbat son")
# elif a>0:
#     print("a soni musbat son")
# elif b>0:
#     print(" b soni musbat son")
# else:
#     print("ikkala son ham manfiy son")


#------------------------------------------------------

#17-masala:

# a = int(input("a sonini kiriting: "))


# if (10 <= a <= 99) and (a % 2 == 0):
#     print("Son ham juft, ham 2 xonali.")
# elif (10 <= a <= 99) and (a % 2 != 0):
#     print("Son 2 xonali, lekin juft emas (toq son).")
# elif (a % 2 == 0):
#     print("Son juft, lekin 2 xonali emas.")
# else:
#     print("Son juft ham emas, 2 xonali ham emas.")

#---------------------------------------------------------


#18-masala:

# a = int(input("a sonini kiriting: "))

# if (100 <= a <= 999) and (a % 2 != 0):
#     print("Son ham toq, ham 3 xonali.")
# elif (100 <= a <= 999) and (a % 2 == 0):
#     print("Son 3 xonali, lekin toq emas (juft son).")
# elif (a % 2 != 0):
#     print("Son toq, lekin 3 xonali emas.")
# else:
#     print("Son toq ham emas, 3 xonali ham emas.")




#19-masala:


# a = (input("uch xonali son kiriting: "))

# birinchi = a[0]
# ikkinchi = a[1]
# uchinchi = a[-1]

# if birinchi != ikkinchi and ikkinchi != uchinchi and birinchi != uchinchi:
#     print("barcha raqamlar har xil")
# else:
#     print("raqamlar ichida bir xillari bor")




#20-masala:


# a = int(input("son kiriting: "))

# if a > 0:
#     print("son musbat")
#     musbat_son=a
# else:
#     print("son manfiy")
#     musbat_son=-a


# if 1 < musbat_son <=9:
#     print("1 xonali son")
# elif 10 < musbat_son <99:
#     print("2 xonali son");
# elif 100 < musbat_son < 999:
#     print("3 xonali son")
# else:
#     print("son berilgan oraliqdan katta")





#21-masala:

# a = (input("son kiriting: "))


# birinchi = a[0]
# ikkinchi = a[1]
# uchinchi = a[-1]

# if birinchi < ikkinchi < uchinchi:
#     print("raqamlar osish tartibida.")
# else:
#     print("raqamlar osish tartibida emas,")







# shoxruh -notion 
#1-masala:
# sum=0

# for i in range(1,6):
#     narx=int(input("narxni kiriting: "))
#     sum+=narx
# print(sum)
#---------------------------------------------


#2-masala:
# sum=0

# for i in range(1, 6):
#     baho=int(input("bahoni kiriting:"))
#     sum+=baho
# natija=sum/5
# print(natija)
#---------------------------------------------------------




#3-masala:
# pul= 1000000/100*10
# sum = 1000000

# for i in range(1, 6):
#     sum += pul
#     print(sum)
#------------------------------------------------------






































#uy ishi: 1-masala:

# n = int(input("Butun son kiriting: "))
# yigindi = 0

# for i in range(1, n + 1):
#     yigindi = yigindi + i ** i
# print(f"Yigindi: {yigindi}")
#----------------------------------------------------------------


#2-masala:
# for i in range(1, 201):
#     print(i)
#     if  '16'==str(i):
#         print("sizning yoshingiz")
#----------------------------------------------------------------------





#3-masala:
# for i in range(100, 1000):
#     son=str(i)

#     a=son[0]
#     b=son[1]
#     c=son[-1]

#     if (a==b and b!=c) or (a==c and a!=b) or (b==c and a!=b):
#         print(i)
#--------------------------------------------------------------------------




#4-masala:
# n = int(input("son kiriting: "))
# import random
# son = random.randint(1, n)

# for i in range(1, 4):
#     num = input("taminiy son kiriting: ")
#     if num == son:
#         print("winner")
#         break
# else:
#         print("loser")
#-----------------------------------------------------------------------------




#notion 4-masala:
# age = int(input("Yoshingizni kiriting: "))
# year = int(input("Nechchi yil obuna bolganizni kiriting: "))
# oylik = 15

# if age>=50:
#     oylik*=0.8

# if year==3:
#     oylik*=0.9
# elif year>=5:
#     oylik*=0.85

# print(oylik)
#--------------------------------------------------------------




#5-misol:
# while True:
#     parol = input("Parol kiriting: ")

#     if len(parol) < 8:
#         print("Parol juda qisqa.")
        
#     katta = False
#     raqam = False
#     belgi = False

#     for i in parol:
#         if i.isupper():
#             katta = True
#         if i.isdigit():
#             raqam = True
#         if i in "@#$":
#             belgi = True
#     if katta == False:
#         print("Parolda katta harf yoq.")
#     if raqam == False:
#         print("Parolda raqam yoq.")
#     if belgi == False:
#         print("Parolda belgi yoq.")
#     print("Parol kuchli!")
#/////////////////////////////////////////////////////////////////







#6-masala:
# for i in range(1, 4):
#     kompaniya = input(f"{i}-kompaniya nomini kiriting: ")
#     narx = int(input("Narxini kiriting: "))

#     if narx > 100:
#         print(f"{kompaniya} aksiyasi qimmat.")
#     elif narx < 50:
#         print(f"{kompaniya} aksiyasi arzon.")
#     else:
#         print(f"{kompaniya} aksiyasi o'rtacha.")




