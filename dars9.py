import json
# 1-masala:
# f = open("test.json")
# natija = json.load(f)

# f = open("test.json")
# for i in natija:
#     if "Matematika" in i["subjects"]:
#         print(i)
# f.close()
#-----------------------------------





# 2-masala
# with open("test.json", "r") as f:
#     natija = json.load(f)
#     a=0
#     for i in natija:
#         a += i["narx"]*i["son"]
# print(a)
#-------------------------------------------





#3-masala:
# f = open("test.json", "r")
# natija = json.load(f)

# print(max(natija,key=lambda x:x["son"]))
# f.close()
#-------------------------------------------------






#4-masala:
# f = open("test.json", "r")
# natija = json.load(f)

# for i in natija:
#     if 500 < i["price"] < 1000 and i["is_available"] == True:
#        print(f"{i["id"], i["material"]}")

# f.close()
#-----------------------------------------------







#5-masala:
# with open("test.json") as f:
#     material = input(">> ")
#     lst = []
#     for i in json.load(f):
#         if material == i['material'] and i['is_available']:
#             lst.append(i)
#     lst.sort(key=lambda x: x['price'])
#     print(lst)





# 6-masala:
# with open("test.json", "r") as f:
#     natija = json.load(f)
#     for i in natija:
#         if i["price"]<1000 and i["is_available"]==False:
#             print(f"{i["material"]}")
#------------------------------------------------






#7-masala:
# f = open("test.json")
# natija = json.load(f)

# for student in natija:
#     for fan in natija[student]:
#         baholar = natija[student][fan]
#         ortacha = sum(baholar) / len(baholar)

#         print(student, fan, ortacha)
# ----------------------------------------------





#file 1-masala:
# f = open("test.json", "r")
# natija = json.load(f)
# f.close()

# f = open("test.json", "w")
# json.dump(natija, f, indent=4)
# f.close()
#---------------------------





#2-masala:
# with open("test.json", "r") as f:
#     natija = json.load(f)
#     yakun = 0
#     for i in natija:
#         sum = 0
#         chegirma = 0
#         sum=i["price"]*i["quantity"]
#         chegirma = sum *i['discount']/100
#         yakun += sum-chegirma
#     print(yakun)
# ==========================================







#3-masala:
# with open("test.json", "r") as f:
#     natija = json.load(f)

# with open("critical_alerts.json", "w") as f:
#     for i in natija:
#         if i['severity']>=7:
#             json.dump(i, f, indent=4)
# ===========================






#4-masala:
# with open("test.json") as f:
#     dct = {}
#     avg=0
#     n=0
#     natija = json.load(f)
#     for i in natija:
#         dct[i['city']]=i['temperature']
#         avg+=i['temperature']
#         n+=1
#     print(f"eng issiq shahar: {max(dct.items(), key=lambda x: x[1])}")        
#     print(f"eng sovuq shahar: {min(dct.items(), key=lambda x: x[1])}")        
#     print(f"ortacha harorat: {avg//n}C")
#--------------------------------------------------





#5-masala:
with open("test.json") as f:
    dct = {}
    avg=0
    n=0
    natija = json.load(f)
    for i in natija['students']:
        scores=i['scores']
        print(scores)
        















#uy ishi:
#notion 1-masala:
# with open("test.json", "r") as f:
#     dct = {}
#     natija = json.load(f)
#     for i in natija:
#       for x in i['items']:
#         #  print(x)
#          sum = 0
#          sum = x['price']*x['quantity']
#          dct[x['product']]=sum
#     # print(dct)
#     print(f"{i['customer_name']}: {max(dct.items(), key=lambda x: x[1])}")
# =====================================








#2-masala:
# with open("test.json", "r") as f:
#     dct = {}
#     natija = json.load(f)
#     for i in natija:
#         # if i['category']=='Pizza':
#         #     print(i)
#         dct[i['name']]=i['price']
#     print(f"eng qimmat ovqat: {max(dct.items(), key=lambda x: x[1])}")
#     print(f"eng arzon ovqat: {min(dct.items(), key=lambda x: x[1])}")
#=============================================






#3-masala:
# with open("test.json", "r") as f:
#     dct = {}
#     jami=0
#     natija = json.load(f)
#     for i in natija:
#         if i['from']=='Tashkent':
#             # print(i)
#             dct[i['flight']]=i['price']
#             jami+=i['seats']
#     print(f"eng qimmat reys: {max(dct.items(), key=lambda x: x[1])}")
#     print(f"eng arzon reys: {min(dct.items(), key=lambda x: x[1])}")
#     print(f"umumiy toshkentdan uchadgan reyslardagi mavjud orinlar soni: {jami}")
#==========================================




#4-masala:
# with open("test.json", "r") as f:
#     dct = {}
#     avg=0
#     soni=0
#     natija = json.load(f)
#     for i in natija:
#         # print(f"{i['city']}da ob havo: {i['temperature']} gradus")
#         dct[i['city']]=i['temperature']
#         avg+=i['temperature']
#         soni+=1
        
        
#     print(f"eng issiq viloyat: {max(dct.items(), key=lambda x: x[1])}")
#     print(f"eng sovuq viloyat: {min(dct.items(), key=lambda x: x[1])}")
#     print(f"20 ta shahar uchun ortacha havo haroarati: {avg//soni}")
#-----------------------------------------------






#5-masala:
# with open("test.json", "r") as f:
#     dct = {}
#     lst =[]
#     python=0

#     natija = json.load(f)
#     for i in natija:
#         if 'Python' in i['courses']:
#             lst.append(i)
#     print(f"python kurslariga qatnashadgan oquvchilar: {lst}")









#5-masala davomi: 3-sharti:
# with open("test.json") as f:
#   students = json.load(f)
#   courses = {}

#   for student in students:
#     for course in student["courses"]:
#         if course in courses:
#             courses[course] += 1
#         else:
#             courses[course] = 1

#   print(courses)




























 










    




