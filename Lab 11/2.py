phone_directory = {}


def add_contacts():
    global phone_directory
    phone_directory = {
        "Sarfaraz (Father)": "0312-4567658",
        "Najma (Mother)": "0334-5678901",
        "Mujtaba": "0345-6789012",
        "Umer": "0356-7890123",
        "Ashhad": "0367-8901234",
        "Asher": "0378-9012345",
        "Misbah": "0389-0123456",
        "Ali": "0390-1234567",
        "Basim": "0301-2345678",
        "Maaz": "0312-3456789",
        "Fatima": "0323-4567891",
        "Maham": "0334-5678902"
    }
    print("Initial phone directory:")
    for name, number in phone_directory.items():
        print(f"{name}: {number}")


def delete_contact(name):
    if name in phone_directory:
        del phone_directory[name]
        print(f"\n{name} has been deleted from the directory.")
    else:
        print(f"\n{name} is not found in the directory.")
    print(f"\nTotal number of members: {len(phone_directory)}")


add_contacts()
delete_contact("Misbah")
