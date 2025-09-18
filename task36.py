sozlar = []

for i in range(5):
    soz = input("So'z kiriting: ")
    sozlar.append(soz)

eng_uzun = sozlar[0] 

for soz in sozlar:
    if len(soz) > len(eng_uzun):  
        eng_uzun = soz

print("Eng uzun so'z:", eng_uzun) 
