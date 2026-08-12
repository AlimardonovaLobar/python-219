#module, filter, map


#sinf ishi 1-masala:

# matn = "Python is great and Python is fun. Learning Python is a great experience"
# new={}
# for i in matn.split():
#     if i not in new:
#         new[i]=1
#     else:
#         new[i]+=1
# print(new)
#-------------------------





#2-masala:
# matn = "Python is great and Python is fun. Learning Python is a great experience"
# natija = set(matn)
# print(natija)
#------------------------------------------------






#3-masala:
# matn = "Python is great and Python is fun. Learning Python is a great experience"
# st = set()
# for i in matn:
#     if i.isalpha():
#         st.add(i.lower())
# print(st)


# lst = []
# sozlar = matn.lower().split()
# for i in sozlar:
#     if sozlar.count(i) == 1:
#         lst.append(i)
# print(lst)
#------------------------------------------------------







#4-masala:
# def format_date(date_str: str) ->str:
#    oylar = {
#     "01": "yanvar", 
#     "02": "fevral",
#     "03": "mart",
#     "04": "aprel",
#     "05": "may",
#     "06": "iyun",
#     "07": "iyul",
#     "08": "avgust",
#     "09": "sentyabr",
#     "10": "oktyabr",
#     "11": "noyabr",
#     "12": "dekabr"
#    }
   
#    kun, oy, yil = date.split(".")

#    return f"{int(kun)}  {oylar[oy]} {yil} yil"

    



# date = "01.01.2000"
# natija = format_date(date)
# print(natija)
#-----------------------------------------------








#5-masala:
# def get_top_user(data: list[tuple[str,int]]) -> str:
#     new = {}
#     for i, x in data:
#         if i not in new:
#             new[i]=x
#         else:
#             new[i]+=x
    
#     return max(new, key=new.get)


# data = [
#     ("user1", 50), 
#     ("user2", 60),
#     ("user1", 40),
#     ("user3", 30)
# ]

# print(get_top_user(data))
#-----------------------------------









#6-masala:
# lst = ['32', '9', '123', '1994', '1024', '998', '1998']
# yangi = []

# for i in lst:
#     son = sum(map(int, i))
#     if son % 2 == 0:
#         yangi.append(int(i + str(son)))
#     else:
#         yangi.append(i)
# print(yangi)
#-----------------------------------------------------------































#uy ishi
#1-masala:
# def format_date(date_str: str) ->str:
#    oylar = {
#     "01": "yanvar", 
#     "02": "fevral",
#     "03": "mart",
#     "04": "aprel",
#     "05": "may",
#     "06": "iyun",
#     "07": "iyul",
#     "08": "avgust",
#     "09": "sentyabr",
#     "10": "oktyabr",
#     "11": "noyabr",
#     "12": "dekabr"
#    }
   
#    kun, oy, yil = date.split(".")

#    return f"{int(kun)}-{oylar[oy]} {yil}-yil"

    



# date = "01.01.2000"
# natija = format_date(date)
# print(natija)
#-------------------------------------------------------










#2-masala:
# def get_top_user(data: list[tuple[str,int]]) -> str:
#     new = {}
#     for i, x in data:
#         if i not in new:
#             new[i]=x
#         else:
#             new[i]+=x
    
#     return max(new, key=new.get)


# data = [
#     ("user1", 50), 
#     ("user2", 60),
#     ("user1", 40),
#     ("user3", 30)
# ]

# print(get_top_user(data))
#----------------------------------------------------------------











#3-masala:
# def count_passing_students(grades:list[int], passinggrade:int) -> int:
#     count = 0
#     for i in grades:
#         if i>=60:
#             count+=1
#     return count



# grades = [45, 60, 75, 30, 90]
# passingGrade = 60
# print(count_passing_students(grades, passingGrade))
#-------------------------------------------------------





#4-masala:
# def ends_with_gram(words: list[str]) -> list[str]:
#     new=[]
#     for i in words:
#         if i.endswith('gram'):
#             new.append(i)
#     return new




# words = ["telegram", "Instagram", "hello", "program", "diagram", "world"]
# print(ends_with_gram(words))
























#musobaqa
#1-masala:
# lst = [1, 2, 4, 5, 6]
# a = max(lst)
# b = min(lst)

# for i in range(b, a+1):
#     if i not in lst:
#         print(f"yoq son: {i}")
#-------------------------------------




#2-masala:


























