# Simple python script to create a python file for the current epoch day of the year
from datetime import datetime
import os

day_of_year = str(datetime.now().timetuple().tm_yday)
year = str(datetime.now().timetuple().tm_year)
current_day = f"day{day_of_year}_{year}.py"

if os.path.exists(current_day):
    print("Python file already exists for today.")
else:
    f = open(current_day, "w+")
    f.close()
