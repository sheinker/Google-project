from collections import defaultdict
from itertools import combinations



sent1 = "Hello big and beautiful world"
sent2 = "To be or not to be, This is the question"
sent3 = "Be good to everyone, everywhere, everytime"


sent_dict = {sent1: 0, sent2: 1, sent3: 2}
bad_chars = [';', ':', '!', "*", ","]
data = defaultdict(set)



for sentence in sent_dict:
    res = [sentence[x:y] for x, y in combinations(range(len(sentence) + 1), r=2)]
    for i in res:
        for j in bad_chars:
            i = i.replace(j, '')
        if not i.startswith(" ") and not i.endswith(" "):
            data[i].add(sent_dict[sentence])


for item in data:
    print(f'{item}: {data[item]}')

