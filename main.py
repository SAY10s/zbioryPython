# # ORYGINALNA, GORSZA WERSJA
#
# import random
# random.seed(0)
#
# rand1 = []
# rand2 = []
#
# a = 0
# while a < 5:
#     rand1.append(random.randint(1,10))
#     rand2.append(random.randint(1,10))
#     a += 1
#
# print(rand1, rand2)
#
# #różnica
# roznica = []
# roznicaA = []
# roznicaB = []
#
#
# for x in rand1:
#     isRepeated = False
#     for y in rand2:
#         if x == y:
#             isRepeated = True
#     if not isRepeated:
#         roznica.append(x)
#         roznicaA.append(x)
#
# for x in rand2:
#     isRepeated = False
#     for y in rand1:
#         if x == y:
#             isRepeated = True
#     if not isRepeated:
#         roznica.append(x)
#         roznicaB.append(x)
#
# #wspolna
# wspolna = []
# for x in rand1:
#     isRepeated = False
#     for y in rand2:
#         if x == y:
#             isRepeated = True
#     if isRepeated:
#         wspolna.append(x)
#
# for x in rand2:
#     isRepeated = False
#     for y in rand1:
#         if x == y:
#             isRepeated = True
#     if isRepeated:
#         wspolna.append(x)
#
# print("Różnica:", set(roznica))
# print("Różnica między A i B", set(roznicaA))
# print("Różnica między B i A", set(roznicaB))
# print("Wspólna:", set(wspolna))
# print("Suma:", set(rand1 + rand2))


#Wersja po nauczeniu się trochę więcej ("the more you know")

import random
random.seed(0)
liczby1 = set()
liczby2 = set()

a = 0
while a < 5:
    liczby1.add(random.randint(1,10))
    liczby2.add(random.randint(1,10))
    a += 1

print(liczby1, liczby2)
print(f"suma: {liczby1 | liczby2}")
print(f"czesc wspolna: {liczby1 & liczby2}")
print(f"roznica między 1 a 2: {liczby1 - liczby2}")
print(f"roznica między 2 a 1: {liczby2 - liczby1}")
print(f"roznica symetryczna: {liczby1 ^ liczby2}")