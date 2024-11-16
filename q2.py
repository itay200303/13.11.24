
text = """This chocolate cake is rich, moist, and full of delicious chocolate flavor.
To make the cake, you will need chocolate, flour, sugar, eggs, and butter.
After baking the chocolate cake, let the cake cool before adding the chocolate frosting."""
dict_count : dict[str, int] = dict()
for word in text.split():
    dict_count[word] = dict_count.get(word, 0) + 1
print(dict_count)
print(f"most common word is: {word[0]}")
text = """This chocolate cake is rich, moist, and full of delicious chocolate flavor.
To make the cake, you will need chocolate, flour, sugar, eggs, and butter.
After baking the chocolate cake, let the cake cool before adding the chocolate frosting."""
dict_count : dict[str, int] = dict()
for letter in text.lower():
    dict_count[letter] = dict_count.get(word, 0) + 1
print(dict_count)
print(f"most least common letter is: {letter[0]} ")




