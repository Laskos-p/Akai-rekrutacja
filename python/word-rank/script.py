import re


# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2

word_dict = {}

for sentence in sentences:
    words = re.findall(r'\w+', sentence)
    for word in words:
        word = word.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

for i in range(3):
    most_oft_word = max(word_dict, key=word_dict.get)
    print(f'{i+1}. 'f'"{most_oft_word}"'f' - {word_dict[most_oft_word]}')
    word_dict.pop(most_oft_word)


# Good luck! You can write all the code in this file.
