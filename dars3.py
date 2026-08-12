#list
#1-masala:
# lst = ['salom', 5, 4.6]
# for i in lst:
#     print(type(i))
#--------------------------------------------




#2-masala:
# lst = [7, 8, 1, 3, 4, 6, 7, 5]
# new = []
# for index, qiymat in enumerate(lst):
#     if index%2==0:
#         new.append(qiymat*qiymat)
#     else:
#         new.append(qiymat * qiymat * qiymat)
# print(new)
#----------------------------------------







#3-masala:
# lst = [2, 3, 0, 9, 0, 8, 0, 7, 0,  0, 4]

# nol=[]
# nolmas = []
# for i in lst:
#     if i==0:
#         nol.append(i)
#     else:
#         nolmas.append(i)
# print(nolmas+nol)
#------------------------------------------------




#4-masala:
# lst = [2, 1, -4, -9, 0, -5, 8, 3]
# lst.remove(max(lst))
# print(max(lst))
#--------------------------------------------------




#5-masala:
# lst = [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]
# lst=set(lst)
# print(lst)
#----------------------------------------------

#6-masala:
# lst = [11, 33, 50]
# new = ""
# for i in lst:
#     new+=str(i)
# print(new)
#---------------------------------------



#7-masala:
# lst = [1, 1, 3, 4, 4, 5, 6, 7]
# lst2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# lst3 = lst+lst2

# print(sum(lst3)/len(lst3))
#-------------------------------------------------



#8-masala:
# lst = ['ada', 212, False, 4567, 'aziza']
# for i in lst:
#         if str(i)==str(i)[::-1]:
#             print(f"{i} >> palindrom")
#         else:
#             print(f"{i} >> palindrom emas")
#----------------------------------------------------




#9-masala:
# lst = ['abc', 'xyz', "bo'lib", 'aba', '1221']
# count = 0
# for i in lst:
#     if len(i)>=2 and i[0]==i[-1]:
#         count+=1
# print(count)
#------------------------------------------



#10 -masala:
# lst = [23, 44, 56, 99, 111, 23, 54]
# for i in lst.copy():
#     if i%2==0:
#         lst.remove(i)
# print(lst)
#-------------------------------------------



#11-masala:
# lst = [[1, 2, 3], [4, 5, 6], [9, 27], [2, 0, 10], [0, 1], [1], [2, 2, 2]]
# new = []
# max=sum(lst[0])

# for i in lst:
#     if len(i)>=2:
#         sm=sum(i)
    
# print(max([x for x in lst if len(x)>=2], key=sum))
#------------------------------------------------------



#12-masala:
# lst = [1, 2, 3]
# for index, value in enumerate(lst):
#     lst = lst[-1]+1
# print(lst)
#----------------------------------------


# lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# new=[]

# for i in lst:
#     if i in lst2:
#         new.append(i)

# print(set(new))


# lst=[1 ,2 ,3, 4, 5, 6, 7, 8]
# n=3
# new=[]
# lst2=[]
# uzunlik=len(lst)
# uzunlik-=1
# c=1
# for i, q in enumerate(lst):
#     new.append(q)

#     if i==n-1:
#         print(new)
#         lst2.append(new)
#         new.clear()
#         # print(new)
#         n+=3
    # elif uzunlik==i:
    #     lst2.append(new)
    #     print(new)
    
# print(lst2)










#1-masala:
# lst = [10, 20, 30, 40, 50]
# print(f"yigindisi: {sum(lst)}")
# print(f"ortacha qiymati: {sum(lst)//len(lst)}")
#------------------------------------------------




#2-masala:
# lst = [12, 45, 2, 89, 34, 89]

# print(lst.index(max))
# print(lst.index(min))
#--------------------------------------------------



#3-masala:
# lst = [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]
# lst=set(lst)
# print(lst)
#-----------------------------------------------------------



#4-masala:
# lst = [2, 4, 6, 8]
# juft= []
# toq = []

# for i in lst:
#     if i%2==0:
#         juft.append(i)
#     elif i%2==1:
#         toq.append(i)
# print("juftlar: ", juft)
# print("toqlar: ", toq)
#---------------------------------------------






























#uy ishi 1-masala:
# lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# count=0
# for i in lst:
#     if type(i)==int:
#         count+=1
# print(f"Integer tipiga xos bolgan qiymatlar soni: {count}")
#---------------------------------------------------------------------







#2-masala:
# lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# for i in lst.copy():
#     if type(i)==str:
#         lst.remove(i)
# print(f" list ichidagi eng katta son bu: {max(lst)}")
#------------------------------------------------------------------------





#3-masala:
# lst = ['abc', 'xyz', "bo'lib", 'aba', '1221']
# count=0
# for i in lst:
#     if len(i)>=2 and i[0]==i[-1]:
#         count+=1
# print(f"LIST ICHIDGI QIYMATLARNING UZUNLIGI 2 VA UNDAN ORTIQ VA BIRINCHI VA OXIRGI BELGISI BIR XIL BOLGAN QIYMATLAR SONI: {count}")
#----------------------------------------------------------------------------





#4-masala:
# lst = [True, "Salom", 5, 5.6]
# for i in lst:
#     print(f"{i} -> {type(i)}")
#-------------------------------------------------------





#5-masala:
# lst = [7, 8, 1, 3, 4, 6, 7, 5]
# new = []
# for index, qiymat in enumerate(lst):
#     if index%2==0:
#         new.append(qiymat*qiymat)
#     else:
#         new.append(qiymat * qiymat * qiymat)
# print(new)
#------------------------------------------------------





#6-masala:
# lst = [2, 1, -4, -9, 0, -5, 8, 3]
# lst.remove(max(lst))
# print(f"Ikkinchi eng katta son: {max(lst)}")
#--------------------------------------------------------------





#7-masala:
# lst = [1, 1, 3, 4, 4, 5, 6, 7]
# lst2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
# lst3 = lst+lst2
# print(f" ikki listning ortacha qiymati: {sum(lst3)/len(lst3)}")
#------------------------------------------------------------------






#8-masala:
# lst = ["ada", 212, False, 4567, "aziza"]
# for i in lst:
#         if str(i)==str(i)[::-1]:
#             print(f"{i} >> palindrom")
#         else:
#             print(f"{i} >> palindrom emas")
#----------------------------------------------------------------




#9-masala:
# lst = ['p', 'q']
# n=5
# new = []
# for i in range(1, n+1):
#     for x in lst:
#         new.append(x+str(i))
# print(new)
#-------------------------------------------------------------






#10-masala:
# lst = [5, 7, 8, 9]
# if lst == sorted(lst):
#     print("o'sish tartibi")
# elif lst == sorted(lst, reverse=True):
#     print("kamayish tartibi")
# else:
#     print("Tartibsiz")
#------------------------------------------------------------









#11-masala:
# lst = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# nol=[]
# nolmas = []
# for i in lst:
#     if i==0:
#         nol.append(i)
#     else:
#         nolmas.append(i)
# print(nolmas+nol)
#--------------------------------------------------------






#12-masala:
# lst = [[2, 15, 4], [19, 24, 11], [7, 9, 5], [10, 3, 1]]
# new =[]
# for i in lst:
#     for x, v in enumerate(i):
#         if x%2==1:
#             new.append(v*v)
#         else:
#             new.append(v)

# print(new)
#-------------------------------------------------------------






#13-masala:
# lst = "[10, 20, [300, 400, [5000, 6000], 500], 30, 6000, 40]"
# lst = str(lst)
# lst = lst.replace("6000", "6000, 7000")
# print(lst)



