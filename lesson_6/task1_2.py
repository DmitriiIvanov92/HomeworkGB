""" 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им
запросов по данным файла логов из предыдущего задания."""


with open('../nginx_logs.txt') as file:
    data = []
    spammer = {}
    for line in file:
        splitter = line.split()[0:7]
        data.append((splitter[0], splitter[5].replace('"', ""), splitter[6]))
        spammer.setdefault(splitter[0], 0)
        spammer[splitter[0]] += 1

spammer = sorted(spammer.items(), key=lambda x: x[1], reverse=True)
print(spammer)
