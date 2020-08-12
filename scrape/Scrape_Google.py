# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:04:33 2020

@author: Royan Abida N. Nayoan
"""

import pandas as pd
from requests import get
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from csv import writer
from itertools import zip_longest
import numpy as np

delays = [5, 8, 7, 4, 9]
delay = np.random.choice(delays)

data = pd.read_csv('scrap_hellosehat.csv')
meds= data['MEDS'].tolist()


import requests
import random


def gSnippet(med):
    time.sleep(delay)
    query = "kandungan " + med
    query = query.replace(" ","+")
    url = "https://www.google.com/search?q=" + query
    
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    snip = soup.find("div", class_ ="BNeawe s3v9rd AP7Wnd")
    if snip != None:
        result = snip.text
    else:
        result = "kosong"
    row_contents = [result]
    append_list_as_row('scrapres_hellosehat.csv', row_contents)
    return result

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='', encoding="utf-8") as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

b = 0
for i in meds:
    b = b + 1
    print(b)
    temp = gSnippet(i)
    print(temp)