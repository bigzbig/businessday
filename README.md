Business Day
============

Simple tool for calculating working days. Allows you to check whether a day is a day of work, calculate the number of working days between two dates, or check the date of the next or previous working day.


Requirements
------------
    dateutil
    calendar


How to use it?
--------------
    from businessday import BusinessDay

Initializing the object of the BusinessDay class, you can specify two parameters. 
  - custom list of public holidays - default empty
  - the list of days of the week off work - default weekend 

```python
wd = BusinessDay(
        holidays=[
            datetime.datetime.date(2014, 12, 24), 
            datetime.datetime.date(2014, 12, 25)
        ],
        weekdays_off_work=[5,6] # Monday is 0 and Sunday is 6
    )
```

    
Then we have four methods, the usage of which is best illustrated by examples.

### is_business_day

Check if date or datetime is a business day.

```python
wd = BusinessDay(holidays=[datetime.date(2009, 1, 1)])
wd.is_business_day(datetime.date(2009, 1, 1)) # New Year
# True
wd.is_business_day(datetime.date(2009, 3, 29)) # Sunday
# False
wd.is_business_day(datetime.date(2009, 3, 30))
# True
```

### count_business_days

Calculate number of working days between two dates

```python
from businessday.polish_datetime import PolishHolidays

holidays = PolishHolidays(2013).dates + PolishHolidays(2014).dates
wd = BusinessDay(holidays=holidays)
wd.count_business_days(datetime.date(2013, 12, 23), datetime.date(2014, 1, 7))
# 8
```

### next
    
You can calculate the date of the third working day following the specified date. This can be useful when calculating the final date for payment by bank transfer or delivery time.

```python
wd = BusinessDay()
wd.next(datetime.date(2009, 3, 28), datetime.timedelta(days=3))
# 2009-03-30
```

### preview

This method is analogous to next