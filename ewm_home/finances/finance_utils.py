import os
import re
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ewm_home.settings")
import finances.models as fin_mod


if __name__ == '__main__':
    bt = time.perf_counter()

    et = time.perf_counter()
    print(round(et - bt, 2))
