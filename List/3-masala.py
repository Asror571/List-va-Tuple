# my_list nomli list yaratildi 
my_list = [10, -5, 20, -15, "HELLO", "world", "PYTHON", -8, "Code", 30]

# O'zgaritirilgan elementlarni va yangilangan elementlarni saqlash uchun lsit yaratildi 
my_list2 = []

for a in my_list:                      # For loop yordamida tekshirildi 
    if isinstance(a, int) and a > 0:     # Agar butun son bo'lsa hamda 0  dan katta bo'lsa 
       my_list2.append(a)               # Yangi listga joylaymiz 

    elif isinstance(a, str):            # Agar   string bo'lsa 
        my_list2.append(a.lower())       # uni kishik harflarga aylantirib yangi istga qo'shamiz
       
print(my_list2)                      # Natijani chiqaramiz