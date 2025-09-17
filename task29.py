numbers=[]
for i in range(10):
    num=int(input(f"{i+1}-sonni kiriting: "))
    numbers.append(num)
result=[]
for num in numbers:
    if numbers.count(num) == 1:
        result.append(num)
print(result)