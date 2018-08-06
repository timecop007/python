from HolidayProcessor import HolidayProcessor


class GenBpsHoliday(HolidayProcessor):
    def detail(self, project, current_date, target_date):
        print("  INSERT INTO SC_HOLIDAY ( MARKET_CODE, HOLIDAY_DATE, HOLIDAY_TYPE, UPDATED_BY, UPDATED_DATE )"
              f" VALUES ('MO',TO_DATE('{target_date}','YYYY-MM-DD'),'N','{project}',SYSDATE);")


def main():
    p = GenBpsHoliday()
    p.process()


if __name__ == '__main__':
    main()
