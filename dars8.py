#txt file boshqarish:
#1-fayl masalalari
# f = open("test.txt", "r")
# dct = {}
# for i in f.read().split("\n"):
#     i = i.split(",")

#     if i[-1] not in dct:
#         dct[i[-1]]=1
#     else:
#         dct[i[-1]]+=1
# print(dct)
# f.close()
#-------------------------------------





# f = open("test.txt")
# lst = []
# for i in f.read().split("\n"):
#     if "visa" in i:
#         lst.append(i)
#         lst.sort(key=lambda x: x.split(",")[-1])
# print(lst)
    
# f.close()
#---------------------------------------------------







# f = open('test.txt')

# for i in f.read().split('\n'):
#     karta = i.split(',')[0]
#     if len(set(karta)) == 10:
#         print(i)

# f.close()
#-----------------------------------------












#2-fayl masalalari:
# f = open("test.txt")

# for i in f.read().split('\n'):
#     for x in i.split(',')[2].split("-"):
#         if x.isdigit():
#             break
#     else:
#         print(i)
# f.close()
#-------------------------------------------------------






# f = open("test.txt")
# natija = f.read().split("\n")
# dct = {}
# for i in natija:
#     i=i.split(",")
#     if i[0] not in dct:
#         dct[i[0]]=1
#     else:dct[i[0]]+=1
# print(dct)
# f.close()
#-------------------------------------------





# f = open("test.txt")
# lst = []
# for i in f.read().split('\n'):
#     for x in i.split(',')[-2].split("-"):
#         lst.append(x)
# print(lst)
#     #     if x.isdigit():
#     #         break
#     # else:
#     #     print(i)
# f.close()
#---------------------------------------
















#uy ishi 
cars = open("test.txt", "r").read().split("\n")
birinchi_qator_keraksiz_malumotlar = cars[0].split(',')
rows = [row.split(",") for row in cars[1:]]
# print(birinchi_qator_keraksiz_malumotlar)
# print(rows)

# brandi boyicha eng kop moshnalar:
counter_brand = {}
for row in rows:
    if row[4] in counter_brand:
        counter_brand[row[4]] += 1
    else:
        counter_brand[row[4]] = 1

top_car_by_brand = sorted([(brand, count) for brand, count in counter_brand.items()], key=lambda x: x[1], reverse=True)[0][0]

counter_country = {}
for row in rows:
    if top_car_by_brand == row[4]:
        if row[-1] in counter_country:
            counter_country[row[-1]] += 1
        else:
            counter_country[row[-1]] = 1

top_brand_by_country = sorted([(country, count) for country, count in counter_country.items()], key=lambda x: x[1], reverse=True)
for country, count in top_brand_by_country:
    print(f"davlat: {country}, brandlar soni: {count}")