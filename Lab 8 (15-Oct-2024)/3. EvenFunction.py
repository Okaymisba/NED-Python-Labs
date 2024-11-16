def even(n):
    list_of_numbers = []
    if n < 0:
        return None
    else:
        for i in range(2, n + 1):
            if i % 2 == 0 or i % 3 == 0:
                list_of_numbers.append(i)
        list_of_numbers_in_given_format = ",".join(str(numbers) for numbers in list_of_numbers)
        return list_of_numbers_in_given_format


print(even(17))
