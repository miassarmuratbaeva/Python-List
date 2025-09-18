words=[]
for i in range(5):
    word=input(f"{i+1}-sozni kiriting: ")
    words.append(word)
palindrom=[]
for word in words:
    if word==word[::-1]:  
        palindrom.append(word)
print(palindrom)