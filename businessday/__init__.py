#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from dateutil import rrule
from datemanip import date_to_datetime, start_day


class BusinessDay(object):
    """ Workday date utility functions to extend datetime
    """

    def __init__(self, holidays=[], weekdays_off_work=[5,6]):
        ''' holidays - list of halidays dates
            weekdays_off_work - list of week days as an integers,
            where Monday is 0 and Sunday is 6.
        '''

        self.holidays = set([start_day(d) for d in set(holidays)])
        self.weekdays_off_work = set(weekdays_off_work)


    def is_business_day(self, dt):
        ''' Check if date or datetime is a business day.
        
            >>> from polish_datetime import PolishHolidays
            >>> ph = PolishHolidays(2009)
            >>> wd = BusinessDay(holidays=ph.dates)
            >>> wd.is_business_day(datetime.date(2009, 1, 1)) # New Year
            True
            >>> wd.is_business_day(datetime.date(2009, 3, 29)) # Sunday
            False
            >>> wd.is_business_day(datetime.date(2009, 3, 30))
            True
        '''
        dt = date_to_datetime(dt)
        d = dt.date()
        if not d.weekday() in self.weekdays_off_work or d in self.holidays:
            return True
        return False


    def next(self, dt, timedelta):
        ''' Add timedelta to date or datetime. Skip free time.
            
            >>> from polish_datetime import PolishHolidays
            >>> ph = PolishHolidays(2009)
            >>> wd = BusinessDay(holidays=ph.dates)
            >>> wd.next(datetime.date(2009, 3, 28), datetime.timedelta(days=1))
            datetime.datetime(2009, 3, 30, 0, 0)
        '''
        dt = date_to_datetime(dt)
        num_days = timedelta.days
        while num_days > 0:
            dt += datetime.timedelta(days=1)
            if self.is_business_day(dt):
                num_days -= 1

        if timedelta.seconds > 0:
            dt = dt + datetime.timedelta(seconds=timedelta.seconds)
            while not self.is_business_day(dt):
                dt += datetime.timedelta(days=1)

        return dt


    def preview(self, dt, timedelta):
        ''' Subtract timedelta from the date or datetime of. Skip free time.

            >>> from polish_datetime import PolishHolidays
            >>> ph = PolishHolidays(2009)
            >>> wd = BusinessDay(holidays=ph.dates)
            >>> wd.preview(datetime.date(2009, 3, 31), datetime.timedelta(days=3))
            datetime.datetime(2009, 3, 26, 0, 0)
        '''
        dt = date_to_datetime(dt)
        num_days = timedelta.days
        while num_days > 0:
            dt -= datetime.timedelta(days=1)
            if self.is_business_day(dt):
                num_days -= 1

        if timedelta.seconds > 0:
            dt = dt - datetime.timedelta(seconds=timedelta.seconds)
            while not self.is_business_day(dt):
                dt -= datetime.timedelta(days=1)

        return dt

    def count_business_days(self, dt_start, dt_end):
        ''' Calculate number of working days between two dates
        
            >>> from polish_datetime import PolishHolidays
            >>> holidays = PolishHolidays(2013).dates + PolishHolidays(2014).dates
            >>> wd = BusinessDay(holidays=holidays)
            >>> wd.count_business_days(datetime.date(2013, 12, 23), datetime.date(2014, 1, 7))
            8
        '''
        dt_start = date_to_datetime(dt_start).date()
        dt_end = date_to_datetime(dt_end).date()
        days = list(set(range(0, 7)) - self.weekdays_off_work)
        weekdays = rrule.rrule(
            rrule.DAILY, byweekday=days,
            dtstart=dt_start, until=dt_end
        )
        return len(set(weekdays)-self.holidays)




        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
