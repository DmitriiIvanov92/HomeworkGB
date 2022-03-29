tutors = ('Анастасия', 'Ирина', 'Ульяна', 'Дмитрий', 'Федор', 'Иван', 'Янис')
klass = ('10А', '11А', '11А', '11В', '7Б', '5В')

for tutors, klass in zip(tutors, klass):
    print(tutors, klass)

# gen = ((tutors, klass) for tutors, klass in zip(tutors, klass))
# print(next(gen))
# print(next(gen))
# print(list(gen))
# print(next(gen))

from itertools import zip_longest

if len(tutors) <= len(klass):
    gen_2 = ((tutors, klass) for tutors, klass in zip_longest(tutors, klass))
else:
    raise Exception('Cписок klass меньше списка tutors')
print(gen_2)
print(next(gen_2))
print(next(gen_2))
print(list(gen_2))
print(next(gen_2))
