import json


# dct = {}

# with open("test.json") as f:
    
#     natija = json.load(f)
#     for i in natija['branches']:
#         sum=0
#         # print(i['name'])   : branchlar nomi
#         # for x in i['teachers']:
#         #   if 'Python'==x['subject']:
#         #      print(x)   : faqat python oquvchilari:

#         # print(len(i['students']))    : har bitta branchdagi oquvchilar soni:
#         for x in i['students']:
#         #     dct[x['name']]=x['payment']
#     # print(max(dct.items(), key=lambda x: x[1]))   : eng kop tolov qilyotgan oquvchi:
#         #  sum +=x['payment']
#         #  print(sum)



#            print("salom dunyo") 




# with open("test.json", "r") as f:
#     movies = json.load(f)

# title = input("Film nomi: ")
# director = input("Rejissor: ")
# year = input("Yil: ")
# genre = input("Janr: ")


# movie = {
#         "title": title,
#         "director": director,
#         "year": int(year),
#         "genre": genre
# }
# movies.append(movie)


# with open("movies.json", "w") as f:
#         json.dump(movies, f, indent=4)
# print("Film muvaffaqiyatli qo'shildi!")

























#uyga vazifa:
#birinchi shart:
# with open("test.json") as f:
#     natija = json.load(f)
#     for i in natija['branches']:
#         print(i['name'])





#ikkinchi shart:
# with open("test.json") as f:
#     natija = json.load(f)
#     for i in natija['branches']:
#         for x in i['teachers']:
#             if x['subject']=='Python':
#                 print(f"{x['name']}:  {i['name']}: {x['experience']}")




#uchinchi shart:
# with open("test.json") as f:
#     natija = json.load(f)
#     for i in natija['branches']:
#         print(f"{i['name']}: {len(i['students'])}")




#tortinchi shart:
# dct = {}
# with open("test.json") as f:
#     natija = json.load(f)
#     for i in natija['branches']:
#         for x in i['students']:
#             dct[x['name']]=x['payment']
#     print(f"eng kop tolov qilgan oquvchi: {max(dct.items(), key=lambda x: x[1])}-{i['name']}")




#beshinchi shart:
# tushum=0
# with open("test.json") as f:
#     natija = json.load(f)
#     for i in natija['branches']:
#         for x in i['students']:
#             tushum+=x['payment']
#         print(f"har bir branch boyicha umumiy tushum: {i['name']}: {tushum}")





#oltinchi shart:
# with open("test.json") as f:
#     natija = json.load(f)
#     for i in natija['branches']:
#         for x in i['teachers']:
#             if x['experience']>5:
#                 print(f"{x['name']}: tajribasi {x['experience']} yil")




#yettinchi shart:
# with open("test.json") as f:
#     natija = json.load(f)
#     for i in natija['branches']:
#         for x in i['teachers']:
#             if x['subject']=='Python':
#                 print(i['name'])


