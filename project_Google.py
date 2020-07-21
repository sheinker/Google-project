from collections import defaultdict
from itertools import combinations



sent1 = "Hello big and beautiful world"
sent2 = "To be or not to be, This is the question"
sent3 = "Be good to everyone, everywhere, everytime"


sent_dict = {sent1: 0, sent2: 1, sent3: 2}
bad_chars = [';', ':', '!', "*", ","]
data = defaultdict(set)
# data = {}


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



# for sentence in sent_dict:
#         for i in range(len(sentence)+1):
#             shortSenE = sentence[i:]
#             shortSenS = sentence[:i]
#             if not shortSenS.endswith(" ") or not shortSenE.endswith(" ")\
#                     or not shortSenE.startswith(" ") or not shortSenS.startswith(" "):
#                 data[shortSenS] = sentence
#                 data[shortSenE] = sentence


# for i in range(len(sent_dict)):
#     for j in range(len(sent_dict[i])):
#         for k in range(j+1, len(sent_dict[i])+1):
#             data[sent_dict[i][k:j]].add(i)
#             data[sent_dict[i][j:k]].add(i)




    # while pos != len(sentence):
    #     pos = sentence.find(" ")
    #     pos = sentence.find(" ", pos, len(sentence))
    #     sentence = sentence[pos:]
    #     sentence = sentence[pos:]

# for sentence in sent_dict:


for sentence in sent_dict:
    res = [sentence[x:y] for x, y in combinations(range(len(sentence) + 1), r=2)]
    for i in res:
        for j in bad_chars:
            i = i.replace(j, '')
        if not i.startswith(" ") and not i.endswith(" "):
            data[i].add(sent_dict[sentence])


for item in data:
    print(f'{item}: {data[item]}')

