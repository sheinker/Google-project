from itertools import combinations
from collections import defaultdict
from string import ascii_lowercase

sent1 = "Hello big and beautiful world "
sent2 = "To be or not to be, This is the question"
sent3 = "Be good to everyone, everywhere, everytime"
sent4 = "Good, better, best, never let them rest, Make the good better and the better make the best"
sent5 = "Bee is making honey"
sent6 = "We are learning in Beit - Yaakov"

sent_dict = {sent1: 0, sent2: 1, sent3: 2, sent4: 3, sent5: 4, sent6: 5}
bad_chars = [';', ':', '-', '!', '*', ',', '$', '@']

data = defaultdict(set)
best_sen = {}


def init_data():
    for sentence in sent_dict:
        substr_list = [sentence[x:y] for x, y in combinations(range(len(sentence) + 1), r=2)]
        for substr in substr_list:
            for char in bad_chars:
                substr = substr.replace(char, '')
            if not substr.startswith(" ") and not substr.endswith(" "):
                data[substr.lower()].add(sent_dict[sentence])


def print_data():
    for item in data:
        print(f'{item}: {data[item]}')


def get_data_at_key(key):
    key = key.lower()
    sentences = []
    for k in data[key]:
        sentences.append(list(sent_dict.keys())[k])
    return sorted(sentences)


#def read_file():
#     file = open("demofile.txt", "r")
#     line = file.readline()
#
#     file.close()


def get_five_best_sentences(prefix):
    best_sentences = get_data_at_key(prefix)
    if len(best_sentences) >= 5:
        return best_sentences[:5]
    else:
        for i in replace_char(prefix)[0]:
            best_sen[i] = replace_char(prefix)[1]
        for i in delete_Unnecessary_char(prefix)[0]:
            best_sen[i] = delete_Unnecessary_char(prefix)[1]
        for i in add_missed_char(prefix)[0]:
            best_sen[i] = add_missed_char(prefix)[1]
        a = set(sorted(best_sen, key=best_sen.get, reverse=True))
        a = set(best_sentences).union(a)
        return list(a)[:5]


def get_best_k_completions(prefix):
    info = []
    best_sent = get_five_best_sentences(prefix)
    for sentence in best_sent:
        info.append(AutoCompleteData(sentence))
    return info


# # def get_sentence_score(sentence):
#
#
# # return sentence with high score
# def high_score_sentence(key):
#     result = get_data_at_key(key)
#     max_score = 0
#     sent_index = 0
#     for index, sentence in enumerate(result):
#         score = get_sentence_score(sentence)
#         if score > max_score:
#             max_score = score
#             sent_index = index
#     return result[sent_index]


def replace_char(word):
    for index, char in enumerate(word):
        for i in ascii_lowercase:
            if word.replace(char, i, 1) in data.keys():
                score = 0
                if index < 6:
                    score -= (5 - index % 5)
                else:
                    score -= 1
                score += (len(word) - 1) * 2
                return get_data_at_key(word.replace(char, i, 1)), score

    return [], 0


def delete_Unnecessary_char(word):
    for index, char in enumerate(word):
        if word.replace(char, "", 1) in data.keys():
            score = 0
            if index < 5:
                score -= 10 - index % 5
            else:
                score -= 2
            score += (len(word) - 1) * 2
            return get_data_at_key(word.replace(char, "", 1)), score
    return [], 0


def add_missed_char(word):
    for index, char in enumerate(word):
        for i in ascii_lowercase:
            if word.replace(char, char + i, 1) in data.keys():
                score = 0
                if index < 5:
                    score -= 10 - index % 5
                else:
                    score -= 2
                score += (len(word) - 1) * 2
                return get_data_at_key(word.replace(char, char + i, 1)), score
    return [], 0


class AutoCompleteData:
    def __init__(self, sentence):
        self.completed_sentence = sentence
        self.source_text = "i dont know"
        self.offset = sent_dict[sentence]
        self.score = 0

    def get_completed_sentence(self):
        return self.completed_sentence

    def get_source_text(self):
        return self.source_text

    def get_offset(self):
        return self.offset

    def get_score(self):
        return self.score


if __name__ == '__main__':
    print("Loading the files and preparing the system...")
    init_data()
    text = input("The system is ready, Enter your text: ")
    result = get_best_k_completions(text)
    i = len(result)
    print(f"There are {i} suggestions:")
    for index, item in enumerate(result):
        print(f'{index + 1}. {item.get_completed_sentence()} ({item.get_source_text()} {item.get_offset()})')







