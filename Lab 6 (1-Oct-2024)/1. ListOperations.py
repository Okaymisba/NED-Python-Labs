sample_list = [2, 1, 3, 5, 4, 3, 8]

del sample_list[5]
sample_list.remove(5)
sample_list.sort()
sample_list.insert(4, 5)
sample_list.pop()
sample_list.extend(sample_list)

print(sample_list)
