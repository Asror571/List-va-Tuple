# List va unnig ichida tuple yaratildi 
user = [
    (1,2,3),
    (1,3,3),
    (1,12,45),
]
#  List ni 1 chi indexdagi tuple qiymati a nomli o'zgaruvchiga joylandi 
a = user[1]     
a[1] = '55'   #  O'zgartitishga urinildi 


#Natija
#TypeError: 'tuple' object does not support item assignment