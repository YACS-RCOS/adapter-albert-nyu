from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

from bs4 import BeautifulSoup
import time
import re
#driver = webdriver.Firefox()
#url = 'https://www.linkedin.com/jobs/search/?keywords=coach%20&location=United%20States&locationId=us%3A0'
#driver.get(url)
#soup = BeautifulSoup(driver.page_source, 'html.parser')

#klass = 'jobs-search-results__count-string results-count-string Sans-15px-black-55% pb0 pl5 pr4'
#text = soup.find('div',{'class':klass}).text.split('\n')[1].lstrip()
#print(text)


def parse():
  # Starting URL for Albert
  url = "https://sis.nyu.edu/psc/csprod/EMPLOYEE/SA/c/NYU_SR.NYU_CLS_SRCH.GBL"
  # Start the webdriver and request the URL
  #driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
  driver = webdriver.PhantomJS()
  wait = WebDriverWait(driver, timeout=10)
  driver.get(url)
  #time.sleep(1)
# Parse the page source
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  parseColleges(soup)
  driver.quit()

def parseColleges(soup):
  # Get First College by id
  print(soup.find('div', {'id': 'win0divNYU_CLS_GRP_VW_DESCR254GP$0'})
  # Get all colleges by id using regular expression
  colleges = soup.findAll('div', id=re.compile('^win0divNYU_CLS_GRP_VW_DESCR254GP\$\d+' ))
  print(colleges)
  # Print names of all colleges
  for college in colleges:
	  print(college.text)


parse()