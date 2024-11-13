provinces = ()

num_provinces = int(input("Enter the number of provinces you want to add: "))

for i in range(num_provinces):
    province = input(f"Enter the name of province {i + 1}: ")
    provinces += (province,)

print("Provinces of Pakistan:", provinces)
