import random 
#function, set



#uy ishi 
#1-masala:
def bigger_price(son, lst):
    lst.sort(key=lambda x: x["price"], reverse=True)
    return lst[:son]








#7-masala:
def half(a: int, b: int):
    count = 0
    print(a, end="")

    while a > b:
        a /= 2
        count += 1
        print(" ->", a, end="")
    print()
    return count









#6-masala:

def cash_machine(l1, l2):
    p1 = 3
    p2 = 3

    for i in range(len(l1)):
        if l1[i] == "share" and l2[i] == "share":
            p1 += 2
            p2 += 2

        elif l1[i] == "steal" and l2[i] == "share":
            p1 += 3
            p2 -= 1

        elif l1[i] == "share" and l2[i] == "steal":
            p2 += 3
            p1 -= 1

    return [p1, p2]





#1-masala:
# son=2
# lst=[{'name': 'bread', 'price': 100},
#      {'name': 'wine', 'price': 138},
#      {'name': 'meat', 'price': 15},
#      {'name': 'water', 'price': 1}]

# natija = bigger_price(son, lst)
# print(natija)







#7-masala:
# a = int(input("A = "))
# b = int(input("B = "))
# print(half(a, b))








#6-masala:
l1 = ["share", "share", "share"]
l2 = ["steal", "share", "steal"]

print(cash_machine(l1, l2))
