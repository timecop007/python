import csv
import fileinput
import re
import sys
from datetime import datetime, timedelta

START_TIME = 'START_TIME'
FIELDS = (
    'ORG_CODE', 'JOB_STREAM', 'JOB_STEP', 'DESC', 'START_STATUS', 'END_STATUS', START_TIME, 'END_TIME', 'DURATION')


def job_stat():
    data = {}
    regex = re.compile("^\[(.*)\]\[.*\]\[(\d{4})\]\[(.*)\]\[(.*)\]\[(.*)\]\[(\w)\]$")
    for line in fileinput.input():
        m = regex.search(line)
        if m:
            timestamp = datetime.strptime(m.group(1), "%H:%M:%S.%f")
            status = m.group(6)
            if status in ('P', 'S'):
                data = dict(zip(FIELDS, (*(m.group(i) for i in range(2, 6)), status, None, timestamp)))
            else:
                duration = timestamp - data[START_TIME]
                if duration < timedelta(0):
                    duration += timedelta(1)
                data.update(zip(FIELDS[5:9], (status, data[START_TIME].time(), timestamp.time(), duration)))
                yield data


def gen_csv():
    writer = csv.DictWriter(sys.stdout, FIELDS)
    writer.writeheader()
    writer.writerows(job_stat())


if __name__ == "__main__":
    gen_csv()
