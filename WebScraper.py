from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

Start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Edge("C:/Users/starf/Downloads/PRO-C127-Student-Boilerplate-Code-main/PRO-C127-Student-Boilerplate-Code-main/msedgedriver.exe")
browser.get(Start_url)

time.sleep(1)

scraped_data = []

def Scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")

    star_table = soup.find("table", attrs={"class", "wikitable"})
    
    table_body = star_table.find("tbody")
    
    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = row.find_all("td")
        print(table_cols)
        temp_list = []

        for col_data in table_cols:
            data = col_data.text.strip()
            print(data)
            temp_list.append(data)

        scraped_data.append(temp_list)

Scrape()

stars_data = []

print(len(scraped_data))
for i in range(0, len(scraped_data)):
    Star_name = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Luminosity = scraped_data[i][7]

    data_need = [Star_name, Distance, Mass, Radius, Luminosity]
    stars_data.append(data_need)

headers = ["Name", "Distance", "Mass", "Radius", "Luminosity"]
 
final_data = pd.DataFrame(stars_data, columns=headers)

final_data.to_csv("scraped_data.csv", index=True, index_label="ID")