# 04a - Dictionaries and Tuples

# Coding Challenge 03b.1

numbers = [1,2,3,4,5,6,7,8,9,10]
even_sum = 0
even_count = 0

for num in numbers:
    if (num % 2) == 0:
        even_sum += num 
        even_count += 1
print(f'{even_sum / even_count = }')

# Coding Exercise 04a.1

sentence = 'the quick brown fox jumped over the lazy dog'
# print(f'{sentence[::-1] = }') # not right

# create a list of strings that were separated by spaces
# words = list(sentence.split(' '))
words = []
word = ''
for char in sentence:
    if char == ' ':
        # the current word is done, add it to the list
        words.append(word)
        word = ''
    else:
        # this character is part of the current word
        word += char

words.append(word)
print(f'{words = }')

# reverse the order of this list of strings
# print(f'{words[::-1] = }')
reverse_words = []
for index in range(len(words) - 1, -1, -1):
    # reverse_words.insert(0, words[index])
    reverse_words.append(words[index])
print(f'{reverse_words = }')

# put the strings back into a single string, separated by spaces
# reverse_sentence = ' '.join(words)

reverse_sentence = ''
for word in reverse_words:
    reverse_sentence += word + ' '
print(f'{reverse_sentence.strip() = }')

# dictionaries

pc_part = {
    'price': 383.00,
    'family': 'Ryzen 7',
    'manufacturer': 'AMD',
    'model': '3700X',
}

print(f'{pc_part = }')
print(f'{pc_part["price"] = }')

for key_name in pc_part.keys():
    print(f'{key_name} -> {pc_part[key_name]}')

# Coding Exercise 04a.2

sentence = '''
Canada is a country in North America. Its ten provinces and three territories extend from the Atlantic Ocean to the Pacific Ocean and northward into the Arctic Ocean, making it the world's second-largest country by total area, with the world's longest coastline. Its border with the United States is the world's longest international land border. The country is characterized by a wide range of both meteorologic and geological regions. It is a sparsely inhabited country of 40 million people, the vast majority residing south of the 55th parallel in urban areas. Canada's capital is Ottawa and its three largest metropolitan areas are Toronto, Montreal, and Vancouver.

Indigenous peoples have continuously inhabited what is now Canada for thousands of years. Beginning in the 16th century, British and French expeditions explored and later settled along the Atlantic coast. As a consequence of various armed conflicts, France ceded nearly all of its colonies in North America in 1763. In 1867, with the union of three British North American colonies through Confederation, Canada was formed as a federal dominion of four provinces. This began an accretion of provinces and territories and a process of increasing autonomy from the United Kingdom, highlighted by the Statute of Westminster, 1931, and culminating in the Canada Act 1982, which severed the vestiges of legal dependence on the Parliament of the United Kingdom.'''
words = sentence.split(' ')
word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print(f'{word_frequency = }')
