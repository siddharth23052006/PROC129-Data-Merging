import time
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

scrape_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

webpage = requests.get(scrape_url) 
time.sleep(10)

def scrape2():
  soup = bs(webpage.text, 'html.parser')
  star_tables = soup.find_all('table')
  table_rows = star_tables[7].find_all('tr')
  temp_list = []
  for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
  
  star_names = []
  star_distance = []
  star_mass = []
  star_radius = []
  headers = ["star_names", "star_distance", "star_mass", "star_radius"]

  for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][0])
    star_distance.append(temp_list[i][5])
    star_mass.append(temp_list[i][7])
    star_radius.append(temp_list[i][8])
  
  df = pd.DataFrame(list(zip(star_names, star_distance, star_mass, star_radius)),  columns=headers)
  df.to_csv('Field_Brown_Dwarf_Stars.csv')
scrape2()