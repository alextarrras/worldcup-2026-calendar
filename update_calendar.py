import os
from datetime import datetime
from icalendar import Calendar, Event
import requests

def generate_calendar():
    cal = Calendar()
    cal.add('prodid', '-//WorldCup2026 Bot//RU')
    cal.add('version', '2.0')
    cal.add('x-wr-calname', 'ЧМ-2026 Матчи + Анализ')
    cal.add('x-wr-timezone', 'Europe/Moscow')

    # Пример события с полным описанием
    event = Event()
    event.add('summary', 'Испания - Бразилия • 1/8 финала (пример)')
    event.add('dtstart', datetime(2026, 6, 28, 18, 0))
    event.add('description', '''Коэффициенты Winline: П1 2.10 | X 3.40 | П2 3.30

Анализ: Суперматч! Испания контролирует мяч, Бразилия — контратаки и скорость.

Ключевые игроки (+):
Испания: Педри, Ямал
Бразилия: Винисиус, Родриго

Слабые звенья (-):
Испания: Центральные защитники при стандартах
Бразилия: Оборона на флангах''')
    cal.add_component(event)

    with open('worldcup2026.ics', 'wb') as f:
        f.write(cal.to_ical())
    print('✅ Календарь обновлён')

if __name__ == '__main__':
    generate_calendar()

# Расширьте эту функцию под API-Football + Winline scraping