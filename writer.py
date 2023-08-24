import datetime
a = datetime.datetime.now().year
months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь',
          10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}


def water_write(mas):
    with open('вода_112.txt', 'w') as f:
        f.write(f'Направляю данные потребления горячей и холодной воды по квартире 112'
                f' за {months[datetime.datetime.now().month]} {datetime.datetime.now().year} года:\n')
        f.write('\nГорячая вода\n')
        f.write(f'\n*191-АВ - {mas[2]}')
        f.write(f'\n*92-АВ - {mas[0]}')
        f.write(f'\n*97-АВ - {mas[4]}\n')
        f.write('\nХолодная вода\n')
        f.write(f'\n*54-АВ - {mas[3]}')
        f.write(f'\n*55-АВ - {mas[1]}')
        f.write(f'\n*53-АВ - {mas[5]}')

