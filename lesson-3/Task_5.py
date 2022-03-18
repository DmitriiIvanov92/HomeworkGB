'''Реализовать функцию get_jokes(),
 возвращающую n шуток, сформированных из трех случайных слов,\
  взятых из трёх списков (по одному из каждого):'''

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice

def get_jokes(number, jokes = None):
    jokes = []
    for i in range(number):
        i = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        jokes.append(i)
    return print(jokes)


get_jokes(int(input('Сколько шуток выдать ? ')))