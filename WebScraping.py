import time
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

scrape_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

r = requests.get(scrape_url) 
time.sleep(10)


def scrape():
  headers = ["star_name", "star_distance", "star_mass", "star_radius", "star_luminosity"]

  soup = bs(r.text, "html.parser")
  star_table = soup.find('table')
  temp_list = []
  table_rows = star_table.find_all('tr')
  for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

  star_names = []
  star_distance = []
  star_mass = []
  star_radius = []
  star_luminosity = []

  for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][1])
    star_distance.append(temp_list[i][3])
    star_mass.append(temp_list[i][5])
    star_radius.append(temp_list[i][6])
    star_luminosity.append(temp_list[i][7])

  df2 = pd.DataFrame(list(zip(star_names, star_distance, star_mass, star_radius, star_luminosity)), columns=headers)
  df2.to_csv('Bright_Stars.csv')

scrape()