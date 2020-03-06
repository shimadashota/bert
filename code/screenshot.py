import pdb
import pandas as pd
import pdb
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

options = Options()
options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('window-size=1280,1024')

driver = webdriver.Chrome(options=options)
#df = pd.read_csv("../../corporationClassifier/data/data_all.csv")
df = pd.read_csv("data_all.csv")

link = df['link']

#for i in range(len(link)):
#for i in np.arange(0,5):
    #driver = webdriver.Chrome(options=options)
    #driver.get(link[i])
    #s = str(i).zfill(5)
    #driver.save_screenshot('../data/images/{0}.png'.format(s))
    #driver.quit()
    #print(i)
driver = webdriver.Chrome(options=options)
driver.get(link[319])
s = str(319).zfill(5)
driver.save_screenshot('../data/images/{0}.png'.format(s))
driver.quit()
print(319)
