import io
from pprint import pprint


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}  #strings_positions[(line_number, position)] = line => dict_words[(*words)] = file.txt
        for file_txt in self.file_names:
            with open(file_txt, 'r', encoding='utf-8') as file:
                words = []
                line = file.read().lower()
                punctut =[',', '.', '=', '!', '?', ';', ':', ' - ']
                for punc in punctut:
                    line = line.replace(punc, '')
                words = line.split()
            all_words[file_txt] = words
        return all_words

    def find(self, word):
        dict_pos = {}
        for key, value in self.get_all_words().items():
            dict_pos[key] = value.index(word.lower()) + 1  # Как здесь использовать tell?
        return dict_pos

    def count(self, word):
        dict_count = {}
        for key, value in self.get_all_words().items():
            dict_count[key] = value.count(word.lower())
        return dict_count





finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
