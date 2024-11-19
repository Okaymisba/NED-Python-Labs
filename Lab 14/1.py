list1 = [10, 20, 30]
list2 = [2, 0, 5]

for i in range(len(list1)):
    try:
        if len(list1) != len(list2):
            raise IndexError("Lists are of unequal length. Cannot perform division.")

        result = list1[i] / list2[i]
        print(f"Result of {list1[i]} / {list2[i]} = {result}")

    except IndexError as e:
        print(f"IndexError occurred: {e}. List index is out of range.")
    except ArithmeticError as e:
        print(f"ArithmeticError occurred: {e}. There was an error during the mathematical operation.")
