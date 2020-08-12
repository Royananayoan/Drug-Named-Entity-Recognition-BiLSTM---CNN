# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:07:08 2020

@author: Royan Abida N. Nayoan
"""

import string
from requests import get
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from csv import writer
from itertools import zip_longest

alphabet = string.ascii_lowercase

def scrapeMeds(alphab):
    url = 'https://www.klikdokter.com/obat?alphabet=' + alphab
    response = get(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    html_soup = BeautifulSoup(response.text, 'html.parser')
    
    meds_containers = html_soup.find_all('li', class_ = 'topics-index--section__item')
    
    for job_elem in meds_containers:
        title_elem = job_elem.find('span').text
        link_elem= job_elem.find('a')['href']
        row_contents = [title_elem, link_elem]
        append_list_as_row('ScrapeResult_KlikDokter.csv', row_contents)
        
def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)
        
for alpha in alphabet:
    scrapeMeds(alpha)
        
