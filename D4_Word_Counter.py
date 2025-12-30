#Day 4 project

user_input =input("Enter your sentence: ")

word_list = user_input.split()
num_word = len(word_list)
num_char = len(user_input)

for i in range(num_word):
    word_list[i] = word_list[i].lower()

most_freq_word = word_list[0]
max_count = 0
for i in range(num_word):
    count = word_list.count(word_list[i])
    if count > max_count:
        max_count = count
        most_freq_word = word_list[i]

print(f"Number of words: {num_word}")
print(f"Number of characters: {num_char}(including space)")
print(f"Most used word: {most_freq_word}")