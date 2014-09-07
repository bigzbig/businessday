#!/usr/bin/python
# coding: utf-8
import datetime
from dateutil import easter

TIME_ZONE = 'Europe/Warsaw'

class PolishHolidays(object):
    '''Dni ustawowo wolne od pracy w Polsce.'''
    
    def __init__(self, year):
        # Wielkanoc - pierwsza niedziela po pełni między 22.03 a 25.04
        e = easter.easter(year)

        d = lambda y,m,d: datetime.date(y,m,d)
        t = lambda d: datetime.timedelta(days=d)
    
        self._holidays = (
            # 1 stycznia - Nowy Rok
            (
                '0101', # slug
                d(year,1,1), # date
                u'Nowy Rok', # official label
                None, # Common label
                1, # 1 public 2 religious
                
            ),
            # 6 stycznia - Święto Trzech Króli - od 6 stycznia 2011 r
            (
                '0601',
                d(year,1,6),
                u'Objawienie Pańskie',
                u'Trzech Króli',
                2,
            ),
            # Zmartwychwstanie Pańskie, pot. Wielkanoc
            (
                'e',
                e,
                u'Zmartwychwstanie Pańskie',
                u'Niedziela Wielkanocna',
                2,
            ),
            (
                'e1',
                e+t(1), 
                u'Zmartwychwstanie Pańskie',
                u'Lany poniedziałek',
                2,
            ),
            # 1 maja - Święto Państwowe
            (
                '0105',
                d(year,5,1),
                u'1 maja',
                u'Święto Pracy',
                1,
            ),
            # 3 maja - Święto Narodowe Trzeciego Maja
            (
                '0305',
                d(year,5,3),
                u'Święto Narodowe Trzeciego Maja',
                None,
                1,
            ),
            # pierwszy dzień Zielonych Świątek, - 49 dni po Wielkanocy
            (
                'e49',
                e+t(49),
                u'Zesłanie Ducha Świętego',
                u'Zielone Świątki',
                2,
            ),
            # dzień Bożego Ciała, - 60 dni po Wielkanocy
            (
                'e60',
                e+t(60),
                u'Najświętszego Ciała i Krwi Pańskiej',
                u'Boże Ciało',
                2,
            ),
            # 15 sierpnia - Wniebowzięcie Najświętszej Maryi Panny
            (
                '1508',
                d(year,8,15),
                u'Wniebowzięcie Najświętszej Maryi Panny',
                u'Matki Bożej Zielnej',
                2,
            ),
            # 1 listopada - Wszystkich Świętych
            (
                '0111',
                d(year,11,1),
                u'Wszystkich Świętych',
                u'Święto zmarłych',
                2,
            ),
            # 11 listopada - Narodowe Święto Niepodległości
            (
                '1111',
                d(year,11,11),
                u'Święto Niepodległości',
                None,
                1,
            ),
            # 25 grudnia - pierwszy dzień Bożego Narodzenia
            (
                '2512',
                d(year,12,25),
                u'Narodzenie Pańskie',
                u'Boże Narodzenie',
                2,
            ),
            # 26 grudnia - drugi dzień Bożego Narodzenia
            (
                '2612',
                d(year,12,26),
                u'Dzień św. Szczepana',
                u'Drugi dzień Świąt Bożego Narodzenia',
                2,
            )
        )
        
    @property
    def dates(self):
        return [i[1] for i in self._holidays]

    @property
    def holidays(self):
        return [{
            'id': i[0], 
            'date': i[1], 
            'label': i[2], 
            'common': i[3]} for i in self._holidays]
    
if __name__ == "__main__":
    ph = PolishHolidays(2009)
    print ph.holidays