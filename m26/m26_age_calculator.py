__author__ = 'cjoakim'

import arrow

from .m26_age import M26Age


class M26AgeCalculator(object):

    @classmethod
    def seconds_per_year(cls):
        return float(31557600.0)  # 60 * 60 * 24 * 365.25

    @classmethod
    def milliseconds_per_year(cls):
        return float(cls.seconds_per_year() * 1000.0)

    @classmethod
    def calculate(self, birth_yyyy_mm_dd, as_of_yyyy_mm_dd):
        if birth_yyyy_mm_dd:
            birth_date = arrow.get(birth_yyyy_mm_dd, 'YYYY-MM-DD')
            asof_date  = arrow.get(as_of_yyyy_mm_dd, 'YYYY-MM-DD')
            if birth_date and asof_date:
                birth_ts = birth_date.timestamp
                asof_ts  = asof_date.timestamp
                diff     = float(asof_ts - birth_ts)
                years    = diff / self.seconds_per_year()
                return M26Age(years)
        else:
            return None
