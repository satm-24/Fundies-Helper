## TODO: Add try-catch when scraping data

from bs4 import BeautifulSoup
import requests
import csv

from time import sleep
from random import randint

sourceHW = requests.get('https://course.ccs.neu.edu/cs2500/Homeworks.html').text
sourceLab = requests.get('https://course.ccs.neu.edu/cs2500/labs.html').text

soupHW = BeautifulSoup(sourceHW, 'lxml')
#print(soupHW)
soupLab = BeautifulSoup(sourceLab, 'lxml')
#print(soupLab)

csv_file = open(r'C:\Users\dukyo\Desktop\CS\Fundies Helpers\fundies-helper-react\src\scraper\fundies_scrape.csv', 'w')
csv_fileT = open(r'C:\Users\dukyo\Desktop\CS\Fundies Helpers\fundies-helper-react\src\scraper\fundies_temp.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['homework', 'homework_link'])

csv_writerT = csv.writer(csv_fileT)
csv_writerT.writerow(['lab', 'lab_link'])

mainHW = soupHW.find('div', class_='main')
#print(mainHW.prettify())
mainLab = soupLab.find('div', class_='main')
#print(mainLab.prettify())

for homework in mainHW.find_all('a', class_='toclink'):

    homeworks = homework.text
    print(homeworks)

    hw_id = homework['href']
    homework_link = f'https://course.ccs.neu.edu/cs2500/{hw_id}'
    print(homework_link)

    print()

    csv_writer.writerow([homeworks, homework_link])

    #sleep(randint(1, 3))

print('---------- labs ----------')

for lab in mainLab.find_all('a', class_='toclink'):
    labs = lab.text
    print(labs)

    lab_id = lab['href']
    lab_link = f'https://course.ccs.neu.edu/cs2500/{lab_id}'
    print(lab_link)

    print()

    csv_writerT.writerow([labs, lab_link])

    #sleep(randint(1, 3))

csv_file.close()
csv_fileT.close()

## -----------------------------------------------------------------------------

import pandas as pd

fundies_scrape = pd.read_csv(r'C:\Users\dukyo\Desktop\CS\Fundies Helpers\fundies-helper-react\src\scraper\fundies_scrape.csv')
fundies_temp = pd.read_csv(r'C:\Users\dukyo\Desktop\CS\Fundies Helpers\fundies-helper-react\src\scraper\fundies_temp.csv')
final = pd.concat([fundies_scrape, fundies_temp], axis=1)
print(final)
final.to_csv(r'C:\Users\dukyo\Desktop\CS\Fundies Helpers\fundies-helper-react\src\scraper\fundies_scrape.csv')

import os
os.remove(r'C:\Users\dukyo\Desktop\CS\Fundies Helpers\fundies-helper-react\src\scraper\fundies_temp.csv')