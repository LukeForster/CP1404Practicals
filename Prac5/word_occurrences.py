"""
Word Occurrences
Estimate: 20 minutes
Actual:   40 minutes
"""

user_sentence = input('Please enter a sentence:')

word_to_count = {}
words = user_sentence.split()

for word in words:
    # print(word)
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1

words = list(word_to_count.keys())
words.sort()
# print(words)
# print(word)

width = max(len(word) for word in words)
for word in words:
    print(f'{word:{width}} : {word_to_count[word]}')
