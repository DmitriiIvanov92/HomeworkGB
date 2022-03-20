"""Реализовать функцию get_jokes(),
 возвращающую n шуток, сформированных из трех случайных слов,\
  взятых из трёх списков (по одному из каждого): """

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice, shuffle

# def get_jokes(number, jokes = None):
#     jokes = []
#     for i in range(number):
#         i = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
#         jokes.append(i)
#     return print(jokes)
#
#
# get_jokes(int(input('Сколько шуток выдать ? ')))
# --------------------------------------------------------
def get_jokes_adv(number, repeates=False):
    """def_jokes to return joke"""
    jokes = []
    if not repeates:
        if number > min(len(nouns), len(adverbs), len(adjectives)):
            return 'Error number jokes'
        else:
            shuffle(nouns)
            shuffle(adverbs)
            shuffle(adjectives)
            for i in range(number):
                jokes.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    else:
        for i in range(number):
            i = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
            jokes.append(i)
    return jokes

print(get_jokes_adv(6 ,False))
print(get_jokes_adv(5, False))
print(get_jokes_adv(6, True))
