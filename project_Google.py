
sent1 = "Hello big and beautiful world"
sent2 = "To be or not to be, This is the question"
sent3 = "Be good to everyone, everywhere, everytime"


sent_dict = [sent1, sent2, sent3]
bad_chars = [';', ':', '!', "*", ","]
data = {}
pos = 0

# for sentence in sent_dict:
#     new_sentence = sentence.split()
#     for word in new_sentence:
#         for i in bad_chars:
#             word = word.replace(i, '')
#         if word.lower() not in data:
#             data[word.lower()] = sentence
#         else:
#             if data[word.lower()] != sentence:
#                 data[word.lower()] = data[word.lower()] + ", " + sentence


for sentence in sent_dict:
    for i in range(len(sentence)):
        shortSen = sentence[:i]
        if not shortSen.endswith(" "):
            data[shortSen] = sentence



for item in data:
    print(f'{item}: {data[item]}')