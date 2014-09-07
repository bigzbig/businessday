#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://github.com/ogt/workdays
import datetime, calendar

def date_to_datetime(dt):
    """
        >>> date_to_datetime(datetime.date(2009,3,30))
        datetime.datetime(2009, 3, 30, 0, 0)
        >>> date_to_datetime(datetime.datetime(2009, 3, 30, 20, 30))
        datetime.datetime(2009, 3, 30, 20, 30)
    """
    if isinstance(dt, datetime.datetime):
        return dt
    return datetime.datetime.combine(dt, datetime.datetime.min.time())


def start_day(dt):
    """
        >>> start_day(datetime.datetime(2009,3,30))
        datetime.datetime(2009, 3, 30, 0, 0)
    """
    dt = date_to_datetime(dt)
    return datetime.datetime.combine(dt.date(), datetime.datetime.min.time())


def end_day(dt):
    """
        >>> end_day(datetime.datetime(2009,3,30))
        datetime.datetime(2009, 3, 30, 23, 59, 59, 999999)
    """
    dt = date_to_datetime(dt)
    return datetime.datetime.combine(dt.date(), datetime.datetime.max.time())


def week_range(dt):
    """Find the first & last datetime of the week for the given day.
    Assuming weeks start on Sunday and end on Saturday.
    Returns a tuple of ``(start_date, end_date)``
    Author: bradmontgomery https://gist.github.com/bradmontgomery/5110985

    >>> week_range(datetime.datetime(2009,3,31))
    (datetime.datetime(2009, 3, 29, 0, 0), datetime.datetime(2009, 4, 4, 23, 59, 59, 999999))
    """

    dt = date_to_datetime(dt)
    # isocalendar calculates the year, week of the year, and day of the week.
    # dow is Mon = 1, Sat = 6, Sun = 7
    year, week, dow = dt.date().isocalendar()

    # Find the first day of the week.
    if dow == 7:
        # Since we want to start with Sunday, let's test for that condition.
        start_date = dt
    else:
        # Otherwise, subtract `dow` number days to get the first day
        start_date = dt - datetime.timedelta(dow)

    # Now, add 6 for the last day of the week (i.e., count up to Saturday)
    end_date = start_date + datetime.timedelta(6)

    return (start_day(start_date), end_day(end_date))

def month_range(dt):
    """ 
    Returns boundary datetimes of the mont that dt is in 
    >>> month_range(datetime.date(2012,2,10))
    (datetime.datetime(2012, 2, 1, 0, 0), datetime.datetime(2012, 2, 29, 23, 59, 59, 999999))
    """
    dt = date_to_datetime(dt)
    week_day_no, last_month_day_no = calendar.monthrange(dt.year, dt.month)
    month_start = datetime.datetime(dt.year, dt.month, 1)
    month_end = end_day(datetime.datetime(dt.year, dt.month, last_month_day_no))
    return (month_start, month_end)


def round_time(dt=None, round_to=60):
    """
        Round a datetime object to any time laps in seconds
        dt : datetime.datetime object, default now.
        round_to : Closest number of seconds to round to, default 1 minute.
        Author: Thierry Husson 2012 - Use it as you want but don't blame me.

        >>> round_time(datetime.datetime(2012,12,31,23,44,59,1234), 60*60)
        datetime.datetime(2013, 1, 1, 0, 0)
        >>> round_time(datetime.datetime(2012,12,31,23,44,59,1234), 30*60)
        datetime.datetime(2012, 12, 31, 23, 30)
    """
    if dt == None: 
        dt = datetime.datetime.now()

    seconds = (dt - dt.min).seconds
    # // is a floor division, not a comment on following line:
    rounding = (seconds + round_to / 2) // round_to * round_to
    return dt + datetime.timedelta(0, rounding-seconds, -dt.microsecond)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
