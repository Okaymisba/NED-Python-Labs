lst = [1,2,3,4,5,6,7,8]

middle_index = len(lst) // 2
print(middle_index)

middle_element = lst[len(lst) // 2]
print(middle_element)

lst.append(lst.pop(0))
print(lst)

lst.sort(reverse=True)
print(lst)