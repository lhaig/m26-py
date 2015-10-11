__author__ = 'cjoakim'

import arrow

from .m26_age import M26Age


class M26AgeCalculator(object):

    @classmethod
    def milliseconds_per_year(self):
        return float(31557600000.0)  # 1000 * 60 * 60 * 24 * 365.25

    @classmethod
    def seconds_per_year(self):
        return float(31557600.0)  # 60 * 60 * 24 * 365.25

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
                print("birth_ts: {0}".format(birth_ts))
                print("asof_ts:  {0}".format(asof_ts))
                print("diff:     {0}".format(diff))
                print("years:    {0}".format(years))
                return M26Age(years)
        else:
            return None
