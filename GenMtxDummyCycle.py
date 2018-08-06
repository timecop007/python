from HolidayProcessor import HolidayProcessor


class GenMtxDummyCycle(HolidayProcessor):
    def header(self):
        print('DECLARE')
        print('  DCID MT_TDC_DUMMY_CYCLE.DUMMY_CYCLE_ID%TYPE;')
        super().header()

    def detail(self, project, current_date, target_date):
        print("  INSERT INTO MT_TDC_DUMMY_CYCLE (DUMMY_CYCLE_ID,DATA_VERSION,ORG_CODE,RUN_ON_CYCLE_DATE,"
              "TARGET_CYCLE_DATE,JOB_GROUP_ID,STATUS,CURRENT_JOB_SEQ) VALUES (DCID,0,'5830',"
              f"TO_DATE('{current_date}','YYYY-MM-DD'),TO_DATE('{target_date}','YYYY-MM-DD'),2,'P',10);")
        print("  DCID := DCID + 1;")


def main():
    p = GenMtxDummyCycle()
    p.process()


if __name__ == '__main__':
    main()
