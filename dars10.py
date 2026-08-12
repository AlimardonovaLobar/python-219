import json


dct = {}

with open("test.json") as f:
    
    natija = json.load(f)
    for i in natija['branches']:
        sum=0
        # print(i['name'])   : branchlar nomi
        # for x in i['teachers']:
        #   if 'Python'==x['subject']:
        #      print(x)   : faqat python oquvchilari:

        # print(len(i['students']))    : har bitta branchdagi oquvchilar soni:
        for x in i['students']:
        #     dct[x['name']]=x['payment']
    # print(max(dct.items(), key=lambda x: x[1]))   : eng kop tolov qilyotgan oquvchi:
        #  sum +=x['payment']
        #  print(sum)



           print("salom dunyo") 







