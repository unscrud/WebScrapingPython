# Tutorial do Canal Codigo Fonte do Youtube (https://youtu.be/Vxl5jUltHBo)

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# 1. Pegar o conteúdo HTML a partir da URL
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

option = Options()
option.headless = True
# webdriver.Firefox(options=option) assim executaria em background
driver = webdriver.Firefox()

driver.get(url)

time.sleep(15)
driver.find_element_by_id("onetrust-accept-btn-handler").click()

time.sleep(5)
driver.find_element_by_xpath(
    "//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()

time.sleep(5)
element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

# 2. Parsear o conteúdo HTML - BeaultifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# 3. Estruturar o conteúdo em um Data Frame - Pandas
df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']
print(df)
# 4. Transformar os Dados em um Dicionário de dados próprio
driver.quit()
# 5. Converter e salvar em um arquivo JSON

# Libs que serão utilizadas
# pip install requests2
# pip install pandas
# pip install lxml
# pip install beautifulsoup4
# pip install selenium
