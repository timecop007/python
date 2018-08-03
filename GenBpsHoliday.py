from HolidayProcessor import HolidayProcessor


class GenBpsHoliday(HolidayProcessor):
    def detail(self, project, current_date, target_date) -> None:
        print("INSERT INTO BPS VALUES '{0}' '{1}' '{2}'".format(project, current_date, target_date))


p = GenBpsHoliday()
p.process()
