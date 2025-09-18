def uzun_sozlar(words):
    new_list = [word for word in words if len(word) > 5]
    return new_list
list = ["kitob", "dastur", "AI", "hello", "python"]
result=uzun_sozlar(list)
print(result)
