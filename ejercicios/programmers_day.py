"""
Prints "Happy Programmer's Day!" if the current date (expressed in days)
is equal to 256.
"""

from datetime import datetime

current_day = datetime.now().timetuple().tm_yday

if current_day == 256:
    print("Happy Programmer's Day!")
else:
    print("Keep coding!")