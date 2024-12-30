# Uchta turli o'zgaruvchilarni yaratildi 
a = 10
b = 20
c = 30


if a < b and b < c:
    a, b, c = c, a, b  # Shart bilan birgalikda qiymatlar almashtirildi 

print("a:", a)          #Natijalar chiqarildi
print("b:", b)
print("c:", c)
