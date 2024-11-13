print(
    f"(a) The number of characters in the word \"anachronistically\" is 1 more than the number of characters in the word \"counterintuitive\".")
print(f"{len("anachronistically") == len("counterintuitive") + 1}")

print(f"\n(b) The word \"misinterpretation\" appears earlier in the dictionary than the word \"misrepresentation\".")
print(f"{"misinterpretation" < "misrepresentation"}")

print(f"\n(c) The letter \"e\" does not appear in the word \"ﬂoccinaucinihilipiliﬁcation\".")
print(f"{'e' not in "ﬂoccinaucinihilipiliﬁcation"}")

print(
    f"\n(d)The number of characters in the word \"counterrevolution\" is equal to the sum of the number of characters in words \"counter\" and \"resolution\".")
print(f"{len("counterrevolution") == len("counter") + len("resolution")}")
