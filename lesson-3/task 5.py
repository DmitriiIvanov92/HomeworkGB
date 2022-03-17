'''Реализовать функцию get_jokes(),
 возвращающую n шуток, сформированных из трех случайных слов,\
  взятых из трёх списков (по одному из каждого):'''

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice
def get_jokes(number):
    if number == 1:
        return [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}']
    elif number == 2:
        return [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}',\
               f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}']
    else:
        return [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}',\
               f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}',\
               f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}']


print(get_jokes(3))