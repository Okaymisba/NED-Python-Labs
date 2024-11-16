total_students = 110

only_english = 25
only_spanish = 10
only_french = 11
english_and_spanish_only = 20
english_and_french_only = 17
spanish_and_french_only = 9
all_three = 13

accounted_students = only_english + only_spanish + only_french + english_and_spanish_only + english_and_french_only + spanish_and_french_only + all_three

speak_none = total_students - accounted_students

english_and_spanish_but_not_french = english_and_spanish_only

french_but_neither_english_nor_spanish = only_french

only_one_language = only_english + only_spanish + only_french

exactly_two_languages = (
        english_and_spanish_only +
        english_and_french_only +
        spanish_and_french_only
)

print("(b) Students Who Speak None:", speak_none)
print("(a) Students Who Speak English and Spanish but not French:", english_and_spanish_but_not_french)
print("(c) Students Who Speak French but Neither English nor Spanish:", french_but_neither_english_nor_spanish)
print("(d) Students Who Speak Only One Language:", only_one_language)
print("(e) Students Who Speak Exactly Two Languages:", exactly_two_languages)
