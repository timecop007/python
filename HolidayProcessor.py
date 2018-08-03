import fileinput
from functools import reduce
from datetime import datetime, timedelta


class HolidayProcessor:
    def __init__(self) -> None:
        self.project = ''
        self.holidays = []

    def header(self) -> None:
        print("BEGIN")

    def detail(self, project, current_date, target_date) -> None:
        pass

    def trailer(self) -> None:
        print("END;")

    def get_input(self) -> None:
        for line in fileinput.input():
            line = line.strip()
            if len(line) == 0:
                break
            if fileinput.lineno() == 1:
                self.project = line
            else:
                d = datetime.strptime(line, '%Y-%m-%d').date()
                if len(self.holidays) == 0 or d > self.holidays[-1]:
                    self.holidays.append(d)
                else:
                    raise ValueError('Date list must be in ascending order!')

    def generate(self, project, holidays) -> datetime:
        def gen_one_date(x, y) -> datetime:
            current_date = target_date = x
            while True:
                target_date += timedelta(1)
                if target_date == y:
                    break
                self.detail(project, current_date, target_date)
            return y

        return reduce(gen_one_date, holidays)

    def process(self) -> None:
        self.get_input()
        self.header()
        self.generate(self.project, self.holidays)
        self.trailer()
