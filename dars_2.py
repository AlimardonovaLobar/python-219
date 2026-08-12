# indeksi mavjud bolgan malumot turlarida slicing tushunchasi bor bu nima degani?
# bu - shu indeksdan iborat elementlarni kesish imkoni beradigan xususiyat

# indeksli malumot turlari bularga: list, tuple, str lar kiradi

# indeks nima ? indeks bu elementning joylashuv tartib raqami
# pythonda indekslar 0 dan boshlanadi
# teskarisiga ham indekslangan masalan -1 dan boshlanadi
#  h  e  l  l  o
#  0  1  2  3  4
# -5 -4 -3 -2 -1

# slicing bu - indeks orqali kesish

# word = "allo"
# print(word[0:4]) # [start:stop]
# print(word[4:14])

# # [start:stop:step]
# print(word == word[::-1])

# condition operator - > ==, !=, >, <, >=, <=, in, not, 
password = "1111"
print("Bankomatga xush kelibsiz")
print("1. Uz")
print("2. Ru")
print("3. En")
lang = input("tanlovingizni kiriting: ")

if lang == "1":
    user_password = input("Parolingizni kiriting: ")
    if user_password == password:
        print("1. Naqd pul yechish")
        print("2. Pinkod o'zgaritish")
        choice = input("tanlovingizni kiriting: ")
        if choice == "1":
            money = input("qancha pul yechmoqchisiz: ")
            print(f"Pulingizni oling: {money}")
        elif choice == "2":
            new_password = input("yangi pinkodingizni kiriting: ")
            if len(new_password) < 5:
                password = new_password
                print(f"muvoffaqiyatli {new_password} ga o'zgartirildi")
            else:
                print("uzunligi 4 ta bolishi kere")
    else:
        print("parol xato")


elif lang == "3":
    user_password = input("Enter your password:")
    if user_password == password:
        print("1. Cash Withdrawal")
        print("2. Change PIN")
        choice = input("Enter your choice")
        if choice == "1":
            money = input("How much would you like to withdraw?")
            print(f"Place take your cash: {money}")
        elif choice == "2":
            new_password = input("Enter your new password:")
            if len(new_password) < 5:
                password = new_password
                print(f"{new_password} changed succesfully")
            else:
                print("Must be 4 digits")
    else:
        print("wrong password")

    


