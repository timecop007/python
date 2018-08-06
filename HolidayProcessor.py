import fileinput
from datetime import datetime, timedelta
from functools import reduce


class HolidayProcessor:
    def __init__(self):
        self.project = ''
        self.holidays = []

    def header(self):
        print("BEGIN")

    def trailer(self):
        print("END;")

    def detail(self, project, current_date, target_date):
        pass

    def get_input(self):
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

    def generate(self, project, holidays):
        def one_date(x, y):
            current_date = target_date = x
            while True:
                target_date += timedelta(1)
                if target_date == y:
                    break
                self.detail(project, current_date, target_date)
            return y

        return reduce(one_date, holidays)

    def process(self):
        self.get_input()
        self.header()
        self.generate(self.project, self.holidays)
        self.trailer()
