data = {((1, 'пн'), (2, 'вт')): ['Русский язык', {'пн': '10:00-11:30', 'вт': '11:40-13:10'}, 'К.А. Патрикеева',
                                 'https://us02web.zoom.us/j/86754495063?pwd=STlaaCtKSVE', '1984'],
        ((2, 'пн'), (3, 'ср')): ['Экономика1', {'пн': '11:40-13:10', 'ср': '13:50-15:20'}, 'С.В. Савицкий',
                                 'https://vk.com/away.php?to=https%3A%2F%2Fus02web.zoom.us%2Fj%2F9302461843%3Fpwd%3DQThHakJoTVhiY2gwYnNWMWV5Qkw4QT09&cc_key=',
                                 '-'],
        ((3, 'пн'), (2, 'пт'), (3, 'пт')): ['Экономика2', {'пн': '13:50-15:20', 'пт': ('11:40-13:10', '13:50-15:20')},
                                            'М.А. Грязнов',
                                            'https://vk.com/away.php?to=https%3A%2F%2Fus02web.zoom.us%2Fj%2F87659156044%3Fpwd%3DUHcwbzNxS2RhU21hWnlRV1U3VDlGdz09',
                                            '-'],
        ((4, 'пн'), (1, 'ср'), (2, 'ср'), (1, 'пт')): ['Математика', {
        'пн': '15:30-17:00', 'ср': ('10:00-11:30', '11:40-13:10'), 'пт': '10:00-11:30'}, 'А.Б. Акимов',
                                                       'https://us02web.zoom.us/j/3515530970', '-'],
        ((1, 'вт'), 'a'): ['Обществознание', {'вт': '10:00-11:30'}, 'А.Р. Рахматуллин',
                      'https://us02web.zoom.us/j/2283570012?pwd=WXBsZVY1eG5SZTVvSENnRzZ2cmhtUT09', '-'],
        ((3, 'вт'), (4, 'пт')): ['Английский язык', {'вт': '13:50-15:20', 'пт': '15:30-17:00'}, 'Т.Н. Звездилина',
                                 'https://vk.com/away.php?to=https%3A%2F%2Fus02web.zoom.us%2Fj%2F2734958230%3Fpwd%3DeS9DSjYrS2hLQ2d1SU9yUHA2OUhyZz09&cc_key=',
                                 '-'],
        ((4, 'ср'), (5, 'ср')): ['Литература', {'ср': '15:30-18:00'}, 'А.Ю. Денисов',
                                 'https://us04web.zoom.us/j/2899413065?pwd=N2VCVTRhYWFB', 'N51ak7'],
        ((4, 'вт'), 'a'): ['История', {'вт': '15:30-17:00'}, 'О.П. Пономаренко', 'https://us02web.zoom.us/j/5187163321', '-'],
        ((2, 'чт'), 'a'): ['Информатика', {'чт': '11:40-13:10'}, 'М.С. Густокашин',
                      'https://vk.com/away.php?to=https%3A%2F%2Fus04web.zoom.us%2Fj%2F77144787511%3Fpwd%3DMENKVFBwNXU&cc_key=',
                      '7gxDG9'],
        ((5, 'пн'), 'a'): ['Инглиш (доп)', {'пн': '18:00-19:30'}, 'Соколова Лия', 'https://vk.com/away.php?to=https%3A%2F%2Fus02web.zoom.us%2Fj%2F9713559364&cc_key=', '-']}
pairs = {(590, 690): 1, (691, 790): 2, (791, 920): 3, (921, 1020): 4, (1021, 1300): 5}
maxPairs = {'пн': 4, 'вт': 4, 'ср': 5, 'чт': 2, 'пт': 4}
day, hours, minutes = input().split()
time = int(hours) * 60 + int(minutes)
ans = ['-', '-', '-', '-', '-']
for i in pairs.keys():
    if i[0] <= time <= i[1]:
        pair = pairs[i]
for j in data.keys():
    if (pair, day) in j:
        ans = data[j]
print(f'{ans[0]}\n{ans[1][day]}\n{ans[2]}\n{ans[3]}\n код: {ans[4]}')
if maxPairs[day] >= pair + 1:
    print('--Следующая пара--')
    for m in data.keys():
        if (pair + 1, day) in m:
            ans2 = data[m]
    print(f'{ans2[0]}\n{ans2[1][day]}\n{ans2[2]}\n{ans2[3]}\n код: {ans2[4]}')
# чекпоинт3
