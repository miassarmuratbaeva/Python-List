list=["olma", "banan", "gilos", "shaftoli"]
print(list)
indeks = int(input())
if 0<=indeks<len(list):
    new=input()
    list[indeks]=new
    print(list)
else:
    print("Xatolik!!!")