duration = int(input('Введите число в секундах : '))
if duration < 60:
    print(duration, 'сек.')
elif 60 <= duration < 3600:
    print(duration // 60, 'мин.', duration % 60, 'сек.')
elif 3600 <= duration < 86400:
    print(duration // 3600, 'ч.', (duration % 3600) // 60, 'мин.', duration % 60, 'сек.')
else:
    print(duration // 86400, 'дн.', (duration % 86400) // 3600, 'ч.', (duration % 3600) // 60, 'мин.', duration % 60, 'сек.')

# # ИЛИ
# duration = int(input('Введите число в секундах : '))
# minute = duration // 60
# hours = duration // 3600
# days = duration // 86400
# if duration < 60:
#     seconds = duration
#     print(seconds, 'сек.')
# elif 60 <= duration < 3600:
#     seconds = duration % 60
#     print(minute, 'мин.', seconds, 'сек.')
# elif 3600 <= duration < 86400:
#     seconds = duration % 60
#     minute = minute % 60
#     print(hours, 'час.', minute, 'мин.', seconds, 'сек.')
# else:
#     seconds = duration % 60
#     minute = minute % 60
#     hours = duration % 86400 // 3600
#     print(days, 'дн.', hours, 'час.', minute, 'мин.', seconds, 'сек.')
