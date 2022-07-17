import requests
from bs4 import BeautifulSoup


def binary_search(seq, letter):
    l = 0
    r = len(seq) - 1
    while l < r:
        m = (l + r + 1) // 2
        if seq[m].text[0] == letter or f' {letter.lower()}' in seq[m].text[0]:
            l = m
        else:
            r = m - 1
    return l


def animal_counter():
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'

    letter = 0
    url = "https://inlnk.ru/jElywR"

    page = requests.get(url).text

    animals = {}
    print("Смотрю букву -", alphabet[letter])
    while True:
        soup = BeautifulSoup(page, 'lxml')
        names = soup.find('div', class_='mw-category mw-category-columns').find_all('a')
        while True:
            if names[-1].text[0] == alphabet[letter] or f' {alphabet[letter].lower()}' in names[-1].text:
                # Проверка если запись о животном в википедии начинается не на букву животного а на букву прилагательное
                # Пример - японский полоз. В вики начинается на "Я", хотя животное на "П"
                if not alphabet[letter] in animals.keys():
                    animals[alphabet[letter]] = 0
                animals[alphabet[letter]] += len(names)
                break
            else:
                if not alphabet[letter] in animals.keys():
                    animals[alphabet[letter]] = 0
                last_word_pos = binary_search(names, alphabet[letter])
                animals[alphabet[letter]] += last_word_pos + 1
                names = names[last_word_pos + 1:]
                letter += 1
                if letter >= len(alphabet):
                    return animals
                print("Смотрю букву -", alphabet[letter])

        links = soup.find('div', id='mw-pages').find_all('a')
        for i in reversed(range(len(links))):
            if links[i].text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + links[i].get('href')
                page = requests.get(url).text


print(animal_counter())
