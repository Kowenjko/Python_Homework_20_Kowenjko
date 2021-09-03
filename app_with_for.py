"""
Розробіть програму, яка приймає різні формати дат, та повертає кортеж (year, month, day).

Враховано кількість місяців, кількість днів в місяці + високосний рік
Читає формати (d m Y), (Y m d), (m d Y) -цей формат розуміє коли d > 12 

В даному скрипті  все через цикл, скоротивши попередній код
"""
import re

# Роздільник
sign = '(\.|\/|\-|\.\s)'
# місяці в яких 31 день
mon_31 = '(0[13578]|[13578]|1[02])'
day_31 = '(0[1-9]|[1-9]|[12][0-9]|3[01])'
year = '((18|19|20)[0-9]{2})'
# місяці в яких 30 день
mon_30 = '(0[469]|[469]|11)'
day_30 = '(0[1-9]|[1-9]|[12][0-9]|30)'
# лютий в якому 28 денів
mon_28_29 = '(02|2)'
day_28 = '(0[1-9]|[1-9]|1[0-9]|2[0-8])'
# високосний рік
day_29 = '(29)'
year_29 = '(((18|19|20)(04|08|[2468][048]|[13579][26]))|2000)'
# масив із зразками дат
arr_data = ['2006. 05. 04', '2006-05-04', '2006/05/04', '2006-5-4', '2006/5/4', '4.5.2006', '4-5-2006',
            '4/5/2006', '04.05.2006', '04-05-2006', '04/05/2006', '05.27.2006', '28.02.2004', '29.2.2004', '29/02/2009']


#  Формат для перевірки дат (д.М.рррр,д-М-рррр,д/М/рррр,дд.мм.рррр,дд-ММ-рррр,дд/ММ/рррр)
arr_d_m_y = [day_31+sign+mon_31+sign+year, day_30+sign+mon_30+sign+year,
             day_28+sign+mon_28_29+sign+year, day_29+sign+mon_28_29+sign+year_29, 'd_m_y']
#  Формат для перевірки дат (М/д/рррр)
arr_m_d_y = [mon_31+sign+day_31+sign+year, mon_30+sign+day_30+sign+year,
             mon_28_29+sign+day_28+sign+year, mon_28_29+sign+day_29+sign+year_29, 'm_d_y']
#  Формат для перевірки дат (рррр. ММ. дд,рррр-ММ-дд,рррр/ММ/дд,рррр-М-д,рррр/М/д)
arr_y_m_d = [year+sign+mon_31+sign+day_31, year+sign+mon_30+sign+day_30,
             year+sign+mon_28_29+sign+day_28, year_29+sign+mon_28_29+sign+day_29, 'y_m_d']

# створюємо кортеж


def search_data(data, format, year_start):
    matches = format.finditer(data)
    for match in matches:
        if year_start == 'y_m_d':
            return match.group(1), match.group(4), match.group(6)
        elif year_start == 'd_m_y':
            return match.group(5), match.group(3), match.group(1)
        elif year_start == 'm_d_y':
            return match.group(5), match.group(1), match.group(3)


# Перебираємо масив з датами
def data_format(data, arr):
    result = None
    for item in range(len(arr)-1):
        matches = re.compile(rf'^{arr[item]}$')
        if matches.search(data):
            result = search_data(data, matches, arr[4])
    if result:
        return result
    else:
        return False


# головна функція


def main(data):
    resultat = data_format(data, arr_d_m_y)
    if not resultat:
        resultat = data_format(data, arr_m_d_y)
        if not resultat:
            resultat = data_format(data, arr_y_m_d)
            if not resultat:
                return 'Не знаю такого формату'
            else:
                return resultat
        else:
            return resultat
    else:
        return resultat


rez = []
for item in arr_data:
    rez.append(main(item))
print(rez)
