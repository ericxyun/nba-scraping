import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import count
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

url = 'https://stats.nba.com/leaders/'
browser = webdriver.Safari()
browser.get(url)

# text = ""


# table = browser.find_element_by_css_selector("div[class='nba-stat-table__overlay']")
# table = browser.find_element_by_class_name('nba-stat-table__overlay')
# text = table.text.split('\n')

header = []

RANK = []
PLAYER =[]
GP = []
MIN = []
PTS = []
FGM = []
FGA = []
FG_PERC = []
THREE_PM = []
THREE_PA = []
THREE_P_PERC = []
FTM = []
FTA = []
FT_PERC = []
OREB = []
DREB = []
REB = []
AST = []
STL = []
BLK = []
TOV = []
EFF = []

columns = [RANK, PLAYER, GP, MIN, PTS, FGM, FGA, FG_PERC, THREE_PM, THREE_PA, THREE_P_PERC, FTM,
FTA, FT_PERC, OREB, DREB, REB, AST, STL, BLK, TOV, EFF]





def scrape_page(text):
	for i, j in enumerate(text, -33):
		if (i >= 0 and
	    	i < 1297 and
			i % 26 != 22 and
			i % 26 not in range(24,27)):
			try:
				columns[i % 26].append(j.split())
			except:
				continue
			
			

def scrape_all():
	count = 0
	while count < 6:
		table = browser.find_element_by_css_selector('.nba-stat-table__overflow')
		text = table.text.split('\n')
		print(text[0])
		scrape_page(text)
		try:
			browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/a[2]').click()
			sleep(2)
			#table = browser.find_element_by_class_name('nba-stat-table__overlay')
			#text = table.text.split('\n')
		except:
			print('clicker not working.')
		count += 1
	else:
		browser.quit()

scrape_all()

data = pd.DataFrame(columns)
print(data.columns)



# PLAYER
