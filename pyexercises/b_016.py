from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    output = []
    end_date = datetime(year=2019, month=2, day=27)
    this_date = PYBITES_BORN
    year_date = PYBITES_BORN + timedelta(days=365)
    days_date = PYBITES_BORN + timedelta(days=100)
    while this_date < end_date:
        if year_date < days_date:
            output.append(year_date)
            this_date = year_date
            year_date = year_date + timedelta(days=365)
        else:
            output.append(days_date)
            this_date = days_date
            days_date = days_date + timedelta(days=100)


gen_special_pybites_dates()
