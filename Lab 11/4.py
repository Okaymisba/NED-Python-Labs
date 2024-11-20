favorite_dishes = {
    "Spaghetti": 5,
    "haleem": 4,
    "Sushi": 5,
    "Pizza": 5,
    "Salad": 3,
    "Biryani": 4,
    "Burger": 5
}

dishes_cooked = {
    "Spaghetti": "Monday",
    "haleem": "Tuesday",
    "Pizza": "Wednesday",
    "Steak": "Thursday",
    "Sushi": "Friday",
    "Soup": "Saturday",
    "biryani": "Sunday"
}

cooked_favorites = [dish for dish in favorite_dishes if dish in dishes_cooked]

print(f"You will get {len(cooked_favorites)} favorite dishes cooked this week.\n")
print("The favorite dishes cooked this week are:")
for dish in cooked_favorites:
    print(f"- {dish}")
