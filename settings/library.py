
try:
    import regex
    import calendar
    import datetime
    from bs4 import BeautifulSoup
    import os
    import pandas as pd


except ImportError:
    import os


    os.system('python3 -m pip install --upgrade pip; pip install -r requirements.txt')