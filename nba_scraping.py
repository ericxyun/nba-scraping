import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import datetime
from selenium.webdriver.firefox.options import Options

pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

# options = Options()
# options.headless = True
browser = webdriver.Firefox()


url = 'https://stats.nba.com/players/traditional/?sort=PTS&dir=-1&Season=2018-19&SeasonType=Regular%20Season'
browser.get(url)

print("Script is working on the NBA average data...")

full_text = [[],[],[],[],[],[],[],[],[],[]]
try:
	for i in range(10):
		table = browser.find_element_by_css_selector('.nba-stat-table__overflow')
		text = table.text.split('\n')
		full_text[i].append(text)
		browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/a[2]').click()
		sleep(1)
except:
	print("Something went wrong in the parsing.")
browser.quit()

header = full_text[0][0][0].split(' ')
rank = []
player = []
stats= []
try:
	for j in range(9):
	    for i in range(1, 151, 3):
	        rank.append(full_text[j][0][i])

	    for i in range(2,151, 3):
	        player.append(full_text[j][0][i])

	    for i in range(3,151, 3):
	        stats.append(full_text[j][0][i].split(' '))
except:
	print("Something went wrong in the dataframe.")

data = pd.DataFrame(stats, columns=header[1:])
try:	
	for item in data.drop('TEAM', axis=1).columns:
	    data[item] = data[item].astype('float')
	data['PLAYER'] = player
	data['WLP'] = data['W'] / data['GP']
	data['DATE'] = str(datetime.date.today())
	x = data.columns.tolist()
	x = x[-1:] + x[-3:-2] + x[0:3] + x[-2:-1] + x[3:28] 
	data = data[x]
except:
	print("Something went wrong in the parsing.")
data.to_csv("data/avg/" + str(datetime.date.today()) + "_avg.csv", index=False)


url = 'https://stats.nba.com/players/traditional/?sort=PTS&dir=-1&Season=2018-19&SeasonType=Regular%20Season&PerMode=Totals'
browser.get(url)

print("Scriping is working on the NBA total data...")

full_text = [[],[],[],[],[],[],[],[],[],[]]

try:	
	for i in range(10):
		table = browser.find_element_by_css_selector('.nba-stat-table__overflow')
		text = table.text.split('\n')
		full_text[i].append(text)
		browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/a[2]').click()
		sleep(1)
	browser.quit()
except:
	print('Something went wrong.')
header = full_text[0][0][0].split(' ')
rank = []
player = []
stats= []

try:	
	for j in range(9):
	    for i in range(1, 151, 3):
	        rank.append(full_text[j][0][i])

	    for i in range(2,151, 3):
	        player.append(full_text[j][0][i])

	    for i in range(3,151, 3):
	        stats.append(full_text[j][0][i].split(' '))
except:
	print('Something went wrong.')
data = pd.DataFrame(stats, columns=header[1:])
try:	
	for item in data.drop('TEAM', axis=1).columns:
	    data[item] = data[item].astype('float')
	data['PLAYER'] = player
	data['WLP'] = data['W'] / data['GP']
	data['DATE'] = str(datetime.date.today())
	x = data.columns.tolist()
	x = x[-1:] + x[-3:-2] + x[0:3] + x[-2:-1] + x[3:28] 
	data = data[x]
except:
	print('Something went wrong.')
data.to_csv("data/total/" + str(datetime.date.today()) + "_total.csv", index=False)
