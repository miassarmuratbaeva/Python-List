words=[]
for i in range(5):
    word=input(f"{i+1}-sozni kiriting: ")
    words.append(word)
palindrom=[]
for word in words:
    if word==word[::-1]:  # So'z teskari yozilganda o'ziga teng bo'lishi kerak
        palindrom.append(word)
print(palindrom)