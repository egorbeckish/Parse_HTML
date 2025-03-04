from .library import *


DATE_TIME=r'(?<date>[0-9]{2}\.[0-9]{2}\.[0-9]{4}),\s(?<time>[0-9]{2}:[0-9]{2})'
MONTH={calendar.month_name[month]: month for month in range(len(calendar.month_name))}