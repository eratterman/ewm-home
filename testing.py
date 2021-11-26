import json
import os
from pathlib import Path
import datetime
import calendar
import logging


class Validators(object):
    def __init__(self):
        self.json_file = Path(os.getcwd()) / 'data.json'
        try:
            json_data = json.loads(self.json_file)
        except AttributeError:
            do something
        except Exception as e:
            log
        finally:
            do


def add_records(new_record):
    all_record = [["chemical1", "value1"], ["chemical2", "value2"]]
    new_record = ["chemical3", "value3"]
    if new_record not in all_record:
        all_record += new_record


def find_number_of_days():
    # today = datetime.datetime.today()
    jan_start = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d %H:%M:%S')
    diff = datetime.datetime.now() - jan_start


file_name = 'somefile.log'
log_level = 20