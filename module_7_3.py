from itertools import count


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self) -> dict:
        """Возвращает словарь следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4']}"""
        all_words = {} # пустой словарь
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                text = file.read().lower()
                for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(symbol, '') # убираем знаки пунктуации
            words = text.split() # разбиваем строку (текст) на элементы списка (по умолчанию по пробелу)
            all_words [name] = words # записываем имя файла и список слов из него в словарь
        return all_words

    def find(self, word: str) -> dict:
        """Возвращает словарь, где ключ - название файла,
        значение - позиция первого такого слова в списке слов этого файла"""
        result = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                result[key] = value.index(word.lower()) + 1 #  возвращаем номер элемента в списке
        return result                                           # и записываем его и название файла в словарь


    def count(self, word: str) -> dict:
        """Возвращает словарь, где ключ - название файла,
        значение - количество слов word в списке слов этого файла"""
        res = {}
        for key, value in self.get_all_words().items():
            word_counter = 0 # создаем счетчик
            for i in value:
                if word.lower() == i:
                    word_counter += 1
                res[key] = word_counter #  записываем название файла и кол-во повторений слова word в словарь
        return res

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

