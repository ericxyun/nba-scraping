import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import count
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

RANK = []
TEAM = []
GP = []
W = []
L = []
WIN_PERC = []
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
TOV = []
STL = []
BLK = []
BLKA = []
PF = []
PFD = []
PLUS_MINUS = []

column =[RANK, TEAM, GP, W, L, WIN_PERC, MIN, PTS, FGM, FGA, FG_PERC, THREE_PM, THREE_PA, THREE_P_PERC, FTM, FTA, FT_PERC, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PLUS_MINUS]

column_list =["RANK", "TEAM", "GP", "W", "L", "WIN_PERC", "MIN", "PTS", "FGM", "FGA", "FG_PERC", "THREE_PM", "THREE_PA", "THREE_P_PERC", "FTM", "FTA", "FT_PERC", "OREB", "DREB", "REB", "AST", "TOV", "STL", "BLK", "BLKA", "PF", "PFD", "PLUS_MINUS"]

url = 'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1'
browser = webdriver.Safari()
browser.get(url)
table = browser.find_element_by_class_name('nba-stat-table__overflow')
text = table.text.split('\n')

for i, j in enumerate(text, -61):
    print(i,j)

for i, j in enumerate(text, -61):
    if (i > 0 and
        i < 870 and
        i % 29 != 0):
        try:
            column[(i % 29)-1].append(str(j).split())
        except:
            continue

browser.quit()

df_T = pd.DataFrame(column)
for i , j in enumerate(column_list):
    df_T.rename({i:j}, inplace=True)
df = df_T.T

df_X = df.drop('TEAM', axis=1).applymap(lambda x: x[0])
df_y = df['TEAM']

df_X['TEAM'] = df_y

df = df_X
