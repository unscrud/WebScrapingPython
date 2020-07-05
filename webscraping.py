# Tutorial do Canal Codigo Fonte do Youtube (https://youtu.be/Vxl5jUltHBo)

import time
import requests
import pandas as pd
from bs4 import BeaultifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import options
import json

# 1. Pegar o conteúdo HTML a partir da URL
# 2. Parsear o conteúdo HTML - BeaultifulSoup
# 3. Estruturar o conteúdo em um Data Frame - Pandas
# 4. Transformar os Dados em um Dicionário de dados próprio
# 5. Converter e salvar em um arquivo JSON

# Libs que serão utilizadas
# pip install requests2
# pip install pandas
# pip install lxml
# pip install beautifulsoup4
# pip install selenium
