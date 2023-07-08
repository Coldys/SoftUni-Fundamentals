""" 1. Which Are In? """
searched_str = input().split(', ')
all_words = input().split(', ')
found_words = set()
for word in all_words:
    for string in searched_str:
        if word.find(string) > -1:
            found_words.add(string)

print([w for w in searched_str if w in found_words])
