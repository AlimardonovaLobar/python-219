#tuple, key, sorted, lambda





#sinf ishi 1-masala:
# tpl = ("salom", "quyosh", "yomg'ir", "malina")
# natija=[i for i in tpl if len(i)>5]
# print(natija)
#------------------------------------------




#2-masala:
# lst = [(1,3), (0,2,0),(1,1,1), (0,4), (1,9)]
# new = []
# for i in lst:
#    new=sum(i)
#    print(new)
#------------------------------------------------------




#3-masala:
# lst = [(1,2,3), (2,2), (3,0,0)]

# lst.reverse()
# print(lst)
#------------------------------------------




#4-masala:
# lst = [(1, 2), (2, 3), (3, 4)]
# new =[]
# for i in lst:
#     new.append(list(i))
# print(new)
#------------------------------------------------------





#5-masala:
# tpl = ("ada", 212, False, 4567, 'aziza')
# tpl = list(tpl)
# # print(tpl)
# for i in tpl:
#     if str(i)==str(i)[::-1]:
#         print(f"{i} >>> palindrom")
#     else:
#         print(f"{i} >>> palindrom emas")
#-----------------------------------------------------------






#6-masal:
# lst = [(1, 2), (3, 4), (8, 9)]
# m=[]
# n=[]
# new=[]
# for i in lst:
#     m.append(i[0])
#     n.append(i[1])
# new.append(tuple(m))
# new.append(tuple(n))
# print(new)


#7-masala:
# lst = [(0,2,0,0), (0,3,2,2), (1,3,2,4,3), (4,1,2,4)]
# natija = []
# for i in lst:
#     yangi = []
#     for son in i:
#         yangi.append(i.count(son))
#     natija.append(tuple(yangi))
# print(natija)
#---------------------------------------------------------------






#notion 1-masal:
# n = int(input("Nechta son kiritasiz: "))
# lst = []
# for i in range(n):
#     son = int(input())
#     lst.append(son)

# print(lst)
#------------------------------------------------------


#2-masala:
# new =[]
# n = int(input(">>>>"))
# for i in range(n):
#     son = int(input(""))
#     new.append(son)

# print(f"list uzunligi: {len(new)}")
# print(f"listning oxirgi soni: {new[-1]}")
# print(f"teskari shakli: {new[::-1]}")
#--------------------------------------------------------------




#3-masala:
# lst = []
# sonlar = input("Sonlarni kiriting: ").split()
# for i in sonlar:
#     lst.append(int(i))
# son = int(input("Qidiriladigan sonni kiriting: "))
# if son in lst:
#     print("Ha, bor")
# else:
#     print("Bunday raqam yo'q")
#--------------------------------------------------------





# lst = [(1, 2), (3, 4), (5, 6), ((3, 4))]
# lst = set(lst)

# print(lst)



#4-masala:
# lst = [3, 5, 6, 34, 78, 33, 23]
# lst.remove(lst[0])
# lst.remove(lst[-1])
# print(sorted(lst))
#-----------------------------------------------------






#5-masala:
# lst = [3, 5, 6, 34, 78, 33, 23]
# for i in lst:
#     if i<6:
#         print(i)
#--------------------------------------------------------------






#6-masala:
# import random
# lst = []
# for i in range(20):
#     lst.append(random.randint(1, 100))
# print(lst)
#----------------------------------------------------------------




#7-masala:
# lst = [56, 99, 3, 71, 49, 17, 29, 50, 85, 12, 23, 87, 3, 65, 25, 43, 66, 72, 83, 96]
# print(f"berilgan listning ortacha qiymati: {sum(lst)/len(lst)}")
#-------------------------------------------------------------------





#8-masala:
# lst = [95, 50, 36, 4, 67, 97, 8, 80, 85, 3, 92, 14, 19, 54, 38, 80, 2, 18, 30, 93]
# print(f"eng katta qiymat: {max(lst)}")
# print(f"eng kichik qiymat: {min(lst)}")
#-----------------------------------------------------------------------







#9-masala:
# lst = [1, 6, 12, 17, 24, 25, 26, 30, 42, 52, 53, 54, 55, 58, 65, 68, 75, 83, 90, 95]
# lst.remove(max(lst))
# lst.remove(min(lst))

# print(f"ikkinchi eng katta son: {max(lst)}")
# print(f"ikkinchi eng kichik son: {min(lst)}")
#-----------------------------------------------------------------






#10-masala:
# lst = [2, 5, 8, 11, 14]
# count = 0
# for i in lst:
#     if i%2==0:
#         count+=1
# print(f"juft raqamlar soni: {count}")
#-----------------------------------------------------------




#11-masala:
# lst = [8,9,10]
# lst[1]=17
# print(lst)




# lst = [8, 9, 10]
# lst.extend([4, 5, 6])
# print(lst)




# lst = [8, 9, 10]
# lst.pop(0)
# print(lst)



# lst = [8, 9, 10]
# lst.sort()
# print(lst)


# lst = [8, 9, 10]
# new = []
# for i in lst:
#     new.append(i*2)
# print(new)



# lst = [8, 9, 10]
# lst.insert(3, 25)
# print(lst)
#-----------------------------------------------








































#uy ishi:
#1-masala:
# lst = [1, 2, 33, 5, 6, 7, 7]
# n = 8

# for index, value in enumerate(lst):
#     for index2, value2 in enumerate(lst[index+1: ]):
#        if value + value2 == n:
#            print(f"{index} , {index2+1+index}")
#-----------------------------------------------------------





#2-masala:
# lst = [1, 4, 6, 8]
# new = []
# for i in lst:
#     new.append(i*2)
# print(new)
#----------------------------------------------------------------





#3-masala:
# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# for i in range(len(lst)):
#     a = list(lst[i])
#     a[-1] = 100
#     lst[i] = tuple(a)

# print(lst)
#-------------------------------------------------------------






#4-masala:
# lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]
# for i in lst.copy():
#     if len(i)==0:
#         lst.remove(i)
# print(lst)
#-----------------------------------------------------------







#5-masala:
# lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# lst.sort(key=lambda x: x[1], reverse=True)
# print(lst)
#----------------------------------------------------------------------







#6-masala:
# lst = []
# s = "python 3.0"

# for i in s:
#     lst.append(i)
# print(tuple(lst))
#--------------------------------------------------------------------







#7-masala:
#bir qatorli for:
# lst = [1, 2, 3, 4]
# prefix = "emp"
# natija = [prefix+str(i) for i in lst]
# print(natija)


#kop qatorli for:
# lst = [1, 2, 3, 4]
# new = []
# prefic= 'emp'
# for i in lst:
#     new.append(prefic+str(i))
# print(new)
#-------------------------------------------------------------







#8-masalaa:
# gap = "salom aziz qalaysan"
# lst=[]

# for i in gap.split():
#     lst.append(i)

# lst.sort(key=lambda x: len(x))
# print(lst)
#----------------------------------------------------------------





#9-masala:
# lst = [12, 'salom', 4.5, 'dunyo', True]
# stringlar = []
# for i in lst:
#     if type(i)==str:
#         stringlar.append(i)

# stringlar.sort()
# print(stringlar)
#-----------------------------------------------------------







#10-masala:
# tpl = (-3, 5, 0, 9, -1, 4)
# tpl=list(tpl)
# new=[]
# for i in tpl:
#     if i>0:
#         new.append(i)
# print(tuple(new))
#------------------------------------------------------------------







#11-masala:
# lst = ['salom', 23, 'dunyo', 5, 100, 'python']
# stringlar=[]
# integerlar=[]

# for i in lst:
#     if type(i)==str:
#         stringlar.append(i)
#     elif type(i)==int:
#         integerlar.append(i)
# stringlar.sort()
# integerlar.sort(reverse=True)
# print(f"osish tartibidagi stringla: {stringlar}")
# print(f"kamayish tartibidagi integerlar: {integerlar}")
#--------------------------------------------------------------






#12-masala:
# lst = [(3, 10), (1, 20), (2, 30)]
# lst.sort(key=lambda x: x[0])
# print(lst)
#------------------------------------------------------






#13-masala:
# lst = [1, 2, 3, 4]
# natija=[i**2 for i in lst]
# print(natija)
#----------------------------------------------------------------







#14-masala:
# lst = ['salom', 'dunyo', 'python']
# new=[]
# for i in lst:
#     new.append(i.capitalize())
# print(new)
#-------------------------------------------------------------------





#15-masala:
# tpl = (1, 2, 3, 4, 5)
# tpl = list(tpl)
# print(sum(tpl))









