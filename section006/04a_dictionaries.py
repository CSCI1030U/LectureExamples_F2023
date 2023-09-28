# 04a - Dictionaries and Tuples

# Coding Challenge 03b.1

numbers = [1,2,3,4,5,6,7,8,9,10]
even_sum = 0
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num 
        even_count += 1
print(f'{even_sum / even_count = }')

# Coding Exercise 04a.1

sentence = 'the quick brown fox jumped over the lazy dog'
# print(f'{sentence[::-1] = }')

# generate a list of words from the sentence (separated by spaces)
words = sentence.split(' ')
print(f'{words = }')

# reverse the order of the word list (hint: [::-1])
# reverse_words = words[::-1]
reverse_words = []
# for word in words:
#     reverse_words.insert(0, word)
for index in range(len(words) - 1, -1, -1):
    reverse_words.append(words[index])
print(f'{reverse_words = }')

# combine the (reversed) word list back into a sentence (separated by space)
# reverse_sentence = ' '.join(reverse_words)
reverse_sentence = ''
for word in reverse_words:
    reverse_sentence += word + ' '
print(f'{reverse_sentence.strip() = }')

# Coding Exercise 04a.1

paragraph = "Canada is a country in North America. Its ten provinces and three territories extend from the Atlantic Ocean to the Pacific Ocean and northward into the Arctic Ocean, making it the world's second-largest country by total area, with the world's longest coastline. Its border with the United States is the world's longest international land border. The country is characterized by a wide range of both meteorologic and geological regions. It is a sparsely inhabited country of 40 million people, the vast majority residing south of the 55th parallel in urban areas. Canadas capital is Ottawa and its three largest metropolitan areas are Toronto, Montreal, and Vancouver."
words = paragraph.split(' ')
word_frequency = {}
for word in words:
    if word in word_frequency:
        # the word is already in the frequency dictionary, so increment it
        word_frequency[word] += 1
    else:
        # the word is not in the frequency dictionary, so add it
        word_frequency[word] = 1
print(f'{word_frequency = }')
