# 15 ta elementdan iborat ro'yxat
my_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]

# Dastlabki va oxirgi uchta elementlarni yangi ro'yxatga saqlash
new_list = my_list[:3] + my_list[-3:]

# Yangi ro'yxatni teskari tartibda chop etildi 
print(new_list[::-1])
