name_list=[]
while True:
    name=input("Ism kiriting (to‘xtatish uchun bo‘sh joy yoki Enter): ")
    if name=="":
        break
    name_list.append(name)

print(f"natija{len(name_list)}")