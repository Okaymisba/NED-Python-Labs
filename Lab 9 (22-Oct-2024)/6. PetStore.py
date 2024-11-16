dog = 83
cat = 101
fish = 22
dog_and_cat = 31
dog_and_fish = 8
cat_and_fish = 10
dog_and_cat_and_fish = 6
other_products = 34

dog_only = dog - dog_and_cat - dog_and_fish + dog_and_cat_and_fish
cat_only = cat - dog_and_cat - cat_and_fish + dog_and_cat_and_fish
dog_or_fish = dog + fish - dog_and_fish
total_purchases = dog + cat + fish - dog_and_cat - dog_and_fish - cat_and_fish + dog_and_cat_and_fish + other_products

print("Purchases for a dog product only:", dog_only)
print("Purchases for a cat product only:", cat_only)
print("Purchases for a dog or a fish product:", dog_or_fish)
print("Total purchases:", total_purchases)
