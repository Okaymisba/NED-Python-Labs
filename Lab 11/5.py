def create_guest_list():
    guest_list = []
    num_guests = int(input("Enter the number of guests: "))
    for _ in range(num_guests):
        guest_name = input("Enter guest name: ")
        num_family_members = int(input(f"Enter number of family members for {guest_name}: "))
        guest_list.append((guest_name, num_family_members))
    return guest_list


def compare_guest_lists(list1, list2):
    common_guests = []
    total_guests = 0
    guest_dict = {guest[0]: guest[1] for guest in list2}

    for guest in list1:
        if guest[0] in guest_dict:
            common_guests.append(guest[0])
            total_guests += guest[1] + guest_dict[guest[0]]
            del guest_dict[guest[0]]
        else:
            total_guests += guest[1] + 1

    for guest, members in guest_dict.items():
        total_guests += members + 1

    return common_guests, total_guests


def main():
    print("Enter the list of guests your parents invited:")
    parents_guest_list = create_guest_list()

    print("\nEnter the list of guests you invited:")
    your_guest_list = create_guest_list()

    common_guests, total_guests = compare_guest_lists(parents_guest_list, your_guest_list)

    print("\nCommon guests invited by both your parents and you:")
    print(common_guests)

    print("\nTotal number of guests (including family members):")
    print(total_guests)


main()
