from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def index(req):
    url = "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    table = soup.select('table')[0]
    df = pd.read_html(str(table))[0]
    rows = df.values.tolist()
    return render(req, 'real_time_clock.html', context={'rows': rows})