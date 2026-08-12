#dict


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dct = {}

# for i in range(len(keys)):
#     dct[keys[i]] = values[i]
# print(dct)






# keys = ['apple', 'pear', 'banana', 'apricot']
# values = ['olma', 'shaftoli', 'banan', 'ananas']
# dct = {}
# for i in range(len(keys)):
#     dct[keys[i]] = values[i]
# print(dct)
#---------------------------------------------------------






#notion 1-masala:
# grades = {
#     "Ali": 85,
#     "Vali": 78,
#     "Hasan": 90
# }

# ism = input("ism: ")
# baho = int(input("baho: "))

# if ism in grades:
#     grades[ism]=baho
#     print(grades)
# else:
#     print("bunday talaba topilmadi")
#----------------------------------------------------------






#2-masala:
# store = {
#     "olma": 5000,
#     "banan": 7000
# }

# name = input("mahsulot nomi: ")
# narx = int(input("narx: "))

# if name in store:
#     print("bu mahsulot allaqachon bor")
# else:
#     store[name]=narx
# print(store)
#-------------------------------------------------------







#3-masala;
# employees = {
#     "101": "Ali",
#     "102": "Bobur",
#     "103": "Madina"
# }

# id = input("ID: ")

# if id in employees:
#     employees.pop((id))
# else:
#     print("bunday id topilmadi")
# print(employees)
#----------------------------------------------




#4-masala:
# prices = {
#     "Laptop": 700,
#     "Phone": 350,
#     "Camera": 500
# }


# qimmat = max(prices, key=prices.get)

# print(f"eng qimmati: {qimmat}"")
# print(f"eng qimmat mahsulot narxi: {prices[qimmat]}"")
#----------------------------------------------------------





#5-masala:
# cart = {
#     "olma": 3,
#     "banan": 5,
#     "uzum": 2
# }

# for i in cart:
#     natija= sum(cart.values())
# print(f"jami mahsulotlar soni: {natija}")
#------------------------------------------------------







#6-masala:
# student = {
#     "name": "Aziz",
#     "age": 20,
#     "contact": {
#         "phone": "+998971234567",
#         "email": "aziz@mail.com"
#     }
# }


# print(f"telefon raqami: {student['contact']['phone']}")
#----------------------------------------------------------------







#7-masala:
# dct1 = {"olma": 5000, "banan": 7000}
# dct2 = {"shaftoli": 8000, "olcha": 10000}

# new = dct1 | dct2
# print(new)
#-----------------------------------------------------






#8-masala:
# orders = [
#     {"customer": "Ali", "amount": 15000},
#     {"customer": "Vali", "amount": 22000},
#     {"customer": "Ali", "amount": 8000}
# ]


# new = {}

# for i in orders:
#     if i['customer'] not in new:
#         new[i['customer']] = i['amount']
#     else:
#         new[i['customer']] += i['amount']

# print(new)
#---------------------------------------------------------




#9-masala:
# matn = input("Matn kiriting: ")
# dct = {}
# for soz in matn.split():
#     dct[soz] = dct.get(soz, 0) + 1
# print(dct)
#-----------------------------------------------







#10-masala:
# products = {
#     "Laptop": 700,
#     "Mouse": 25,
#     "Phone": 350,
#     "Camera": 500,
#     "Keyboard": 45
# }
# cheap_products ={}


# for i, x in products.items():
#     if x<100:
#         cheap_products[i]=x
# print(cheap_products)
#----------------------------------------------------









#rasm1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dct = {}

# for i in range(len(keys)):
#     dct[keys[i]] = values[i]
# print(dct)
#--------------------------------------------------




#rasm2
# dct ={'a': 100, 'b': 200, 'c': 300}
# if 100 in dct.values():
#     print("ha bor")
# else:
#     print("yoq")
#-----------------------------------------------



#rasm3:
# dct = {1: 10, 2: 20, 3: 30, 4: 55, 5: 25}
# dct.pop(max(dct, key=dct.get))
# dct.pop(min(dct, key=dct.get))

# print(dct)
#-----------------------------------------------





#rasm4:
# dct1 = {1:10, 2:20}
# dct2 = {3:30, 4:40}
# dct3 = {9:90, 7: 70}
# new = dct1 | dct2 | dct3 
# print(new)
#-------------------------------------






#rasm 5:
# dct = {'data1': 100, 'data2': -54, 'data3': 247}
# natija = sum(dct.values())
# print(natija)
#----------------------------------




#rasm6:
# dct = {9: 10, 2: 20, 3: 30, 4: 55, 1: 25}

# print(sorted(dct.keys()))

# print(sorted(dct))
# print(sorted(dct, key=lambda x: dct[x]))
# print(sorted(dct, key=dct.get))
# print(sorted(dct.items(), key=lambda x: x[1]))
#------------------------------------------------





















#uyga vazifa:
data = [
    {"full_name":"Eugene Elsmor","company":"Kazu","position":"Electrical Engineer","salary":"$4440.86"},
    {"full_name":"Joni Stredder","company":"JumpXS","position":"Environmental Tech","salary":"$870.05"},
    {"full_name":"Terri-jo Fulham","company":"Tagchat","position":"Assistant Media Planner","salary":"$1992.55"},
    {"full_name":"Priscilla Pandya","company":"Youopia","position":"Help Desk Operator","salary":"$3715.95"},
    {"full_name":"Wolfy Swanborough","company":"Topiclounge","position":"Recruiter","salary":"$1045.61"},
    {"full_name":"Raleigh Ratter","company":"Zoozzy","position":"Graphic Designer","salary":"$602.41"},
    {"full_name":"Anastasia Winward","company":"Avaveo","position":"Cost Accountant","salary":"$3641.42"},
    {"full_name":"Dorry Vasyunichev","company":"Fivebridge","position":"Junior Executive","salary":"$2035.05"},
    {"full_name":"Richy Cleft","company":"Jamia","position":"Sales Associate","salary":"$912.98"},
    {"full_name":"Zack Record","company":"Oyonder","position":"Social Worker","salary":"$2492.23"},
    {"full_name":"Lissy Newns","company":"Riffwire","position":"Developer II","salary":"$1177.79"},
    {"full_name":"Audrye Churchyard","company":"Photospace","position":"Environmental Tech","salary":"$4125.83"},
    {"full_name":"Timothy Seligson","company":"Riffpath","position":"Compensation Analyst","salary":"$1271.94"},
    {"full_name":"Brandie Rogeon","company":"Riffpath","position":"Analyst Programmer","salary":"$1911.09"},
    {"full_name":"Dane Rugg","company":"Twimm","position":"Associate Professor","salary":"$2200.72"},
    {"full_name":"Mick Jeduch","company":"Realblab","position":"Executive Secretary","salary":"$1154.20"},
    {"full_name":"Rowland Christofol","company":"Mycat","position":"Senior Cost Accountant","salary":"$1119.94"},
    {"full_name":"Sibella Abrahams","company":"Minyx","position":"Internal Auditor","salary":"$4023.25"},
    {"full_name":"Layne Thomel","company":"Centimia","position":"Research Associate","salary":"$4073.17"},
    {"full_name":"Demetris Clemenzi","company":"Tagopia","position":"Human Resources Manager","salary":"$1530.37"},
    {"full_name":"Kerstin Devon","company":"Katz","position":"Senior Quality Engineer","salary":"$1305.61"},
    {"full_name":"Brandon Burgwyn","company":"Mydeo","position":"Physical Therapy Assistant","salary":"$1325.58"},
    {"full_name":"Dyana Crosby","company":"Riffpath","position":"Payment Adjustment Coordinator","salary":"$1501.54"},
    {"full_name":"Harald Voller","company":"Riffpedia","position":"Accountant I","salary":"$4397.60"},
    {"full_name":"Nollie Phipard-Shears","company":"Aimbo","position":"Legal Professor","salary":"$3172.57"},
    {"full_name":"Gaynor Dannohl","company":"Riffpath","position":"Administrative Assistant II","salary":"$3035.89"},
    {"full_name":"Tome Bensen","company":"Yamia","position":"Assistant Professor","salary":"$3677.10"},
    {"full_name":"Jessey Anshell","company":"Bubblemix","position":"Registered Nurse","salary":"$2782.66"},
    {"full_name":"Valentijn Melbury","company":"Bluejam","position":"Statistician I","salary":"$1308.43"},
    {"full_name":"Rochelle Andrejevic","company":"Riffpath","position":"VP Product Management","salary":"$1734.61"}
]




#1-masala:
# son = 0
# for i in data:
#     if "Human Resources" in i["position"]:
#         son+=1
# print("hunman resouces bolimida ishledgan xodimlar soni: ", son)
#-------------------------------------------------------



#2-masala:
# jami = 0
# for i in data:
#     if "Riffpath" in i["company"]:
#         jami += float(i["salary"].replace("$", ""))

# print(jami)
#----------------------------------------------------------






#3-masala:
# for i in data:
#     if i['full_name'][0] == 'K':
#         i['salary']=float(i["salary"].replace("$", ""))
#         i['salary']= i['salary']*i['salary']
#         print(f"{i['full_name']} ->  ${int(i['salary'])}")
#------------------------------------------------------------------







#4-masala:
# for i in data:
#     i["FIO"] = i.pop("full_name")
# print(data)
#-------------------------------------------------------------






#5-masala:
# new_data = []
# for i in data:
#     if "Senior" not in i["position"] and "Junior" not in i["position"]:
#         new_data.append(i)
# print(new_data)
#--------------------------------------------------------






#6-masala:
# count=0
# for i in data:
#     if 'Assistant' in i['position']:
#         count+=1
# print(count)
#--------------------------------------




#7-masala:
# for i in data:
#     i['position']=replace('Assistant', 'Junior')

# print(data)

















#support: 1-masala:
# javon1 = {"Futbolka": 85000, "Shim": 160000}
# javon2 = {"Kepka": 60000, "Krossovka": 320000}

# natija = javon1 | javon2
# print(natija)







#2-masala:
# orders = [{"name": "Aziz", "sum": 28000}, {"name": "Madina", "sum": 45000}, {"name": "Aziz",
# "sum": 17000}]
# new = {}
# for i in orders:
#     if i['name'] not in new:
#         new[i['name']]=i['sum']
#     else:
#         new[i['name']]+=i['sum']
# print(new)










#3-masala:
# books = ["Python", "C", "Python", "Algoritm", "C", "Python"]
# new={}
# for i in books:
#     if i not in new:
#         new[i]=1
#     else:
#         new[i]+=1
# print(new)








#4-masala:
# cards = {"Ali": 35000, "Vali": 12000, "Sardor": 28000, "Malika": 18000}
# new={}
# for k, q in cards.items():
#     if q>=20000:
#         new[k]=q
# print(new)






#5-masala:
# results = {"Jasur": 87, "Kamron": 94, "Dilshod": 76, "Akmal": 91}
# eng_yuqori = max(results, key=lambda x: results[x])
# eng_past = min(results, key=lambda x: results[x])
# print(f"Eng yuqori: {eng_yuqori} ({results[eng_yuqori]})")
# print(f"Eng past: {eng_past} ({results[eng_past]})")







#6-masala:
# contacts = {"Aziza": "+998901112233", "Bek": "+998933334455"}
# new={}
# for name, number in contacts.items():
#     new[number]=name
# print(new)









#7-masala:
# stipend = {"Ali": 500000, "Zarina": 650000, "Bobur": 400000}
# new={}
# for name, stip in stipend.items():
#     new[name]=stip * 1.10
# print(new)










#8-masala:
# stock = {"Non": {"price": 4000, "qty": 30}, "Somsa": {"price": 7000, "qty": 20}, "Patir": {"price":
# 12000, "qty": 10}}

# jami = 0

# for mahsulot, info in stock.items():
#     qiymat = info["price"] * info["qty"]
#     print(f"{mahsulot} = {qiymat}")
#     jami += qiymat
# print("Umumiy =", jami)










# books = {
#     "Python": {"price": 50000, "qty": 8},
#     "Java": {"price": 65000, "qty": 5},
#     "C++": {"price": 70000, "qty": 4}
# }

# jami=0

# for mahsulot, malumot in books.items():
#     qiymat = malumot['price'] * malumot['qty']
#     print(f"{mahsulot} = {qiymat}")
#     jami+=qiymat
# print("umumiy =", jami)











#9-masala;

# tickets = ["Oddiy", "VIP", "Oddiy", "Talaba", "VIP", "Oddiy", "VIP"]
# new={}

# for i in tickets:
#     if i not in new:
#         new[i]=1
#     else:
#         new[i]+=1
# print(new)










#10-masala:
# students = {"Aziz": [80, 90, 70], "Madina": [95, 90, 100], "Javohir": [75, 80, 85]}
# new = {}
# for k, q in students.items():
#     new[k]=sum(q)/len(q)
# print(new)









#11-masala:
# profile = {"name": "Nodir", "email": "nodir@mail.com", "phone": "", "city": None, "age": 19}

# ochirish = []

# for key, value in profile.items():
#     if value == "" or value is None:
#         ochirish.append(key)

# for key in ochirish:
#     profile.pop(key)

# print(profile)






#12-masala:
# items = [
#     {"name": "Olma", "type": "Meva"},
#     {"name": "Kartoshka", "type": "Sabzavot"},
#     {"name": "Banan", "type": "Meva"},
#     {"name": "Sabzi", "type": "Sabzavot"}
# ]
# result = {}
# for i in items:
#     name = i["name"]
#     type = i["type"]
#     if type not in result:
#         result[type] = []
#     result[type].append(name)
# print(result)

#12 masalani ustozdan sora:










#13-masala:
# d1 = {"Vitamin C": 25000, "Paratsetamol": 12000, "Krem": 30000}
# d2 = {"Paratsetamol": 11000, "Krem": 32000, "Shampun": 28000}

















