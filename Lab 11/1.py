family = {
    "me": {"name": "Misbah"},
    "parents": {"father": "Sarfaraz", "mother": "Najma"},
    "siblings": {"brother": "Mujtaba", "sister": "Ayesha"},
}

for i, item in family.items():
    print(i, item)
print()
family.update({
    "grandparents": {
        "paternal": {"grandfather": "Yaseen", "grandmother": "Fatima"},
        "maternal": {"grandfather": "Imam", "grandmother": "Sana"},
    },
    "uncles_and_aunts": {
        "paternal": {"uncle": "Mumtaz", "aunt": "Shaheen"},
        "maternal": {"uncle": "Kashif", "aunt": "Bushra"},
    }
})

print("Updated Family : ")
print()
for i, item in family.items():
    print(i, item)
