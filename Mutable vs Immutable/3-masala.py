user_new = ['a',56,42,5.5,'b']   # List yaratildi 
user_tuple  = tuple(user_new)  # Listni tuple ga o'zgartirdik 
user_tuple[2] = 'IT'           # Va tuple ro'yxatni o'zgartirishga urindik

print(user_new)
print(user_tuple)


#Natija
#TypeError: 'tuple' object does not support item assignment
