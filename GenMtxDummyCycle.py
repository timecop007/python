from HolidayProcessor import HolidayProcessor


class GenMtxDummyCycle(HolidayProcessor):
    def header(self) -> None:
        print('DECLARE')
        print('  VAR HERE')
        super().header()

    def detail(self, project, current_date, target_date) -> None:
        print("INSERT INTO MTX VALUES '{0}' '{1}' '{2}'".format(project, current_date, target_date))


p = GenMtxDummyCycle()
p.process()
