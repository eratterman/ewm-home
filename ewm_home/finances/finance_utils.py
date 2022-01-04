import os
import re
import time
import pandas
from pathlib import Path
import ewm_home.settings as settings


BASE_DIR = settings.BASE_DIR


class Statements(object):
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.file_name = self.file_path.name


if __name__ == '__main__':
    bt = time.perf_counter()

    print(BASE_DIR)

    et = time.perf_counter()
    print(round(et - bt, 2))
