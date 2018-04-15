from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

from bs4 import BeautifulSoup
import time
import re

def parse():
  # Starting URL for Albert
  url = "https://sis.nyu.edu/psc/csprod/EMPLOYEE/SA/c/NYU_SR.NYU_CLS_SRCH.GBL"
  # Start the webdriver and request the URL
  #driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
  driver = webdriver.PhantomJS()
  wait = WebDriverWait(driver, timeout=10)
  driver.get(url)
  time.sleep(1)
# Parse the page source
  soup = BeautifulSoup(driver.page_source )
  parseColleges(soup)
  driver.quit()

def parseColleges(soup):
  # Get First College by id
  print(soup.find('div', {'id': 'win0divNYU_CLS_GRP_VW_DESCR254GP$0'}))
  # Get all colleges by id using regular expression
  colleges = soup.findAll('div', id=re.compile('^win0divNYU_CLS_GRP_VW_DESCR254GP\$\d+' ))
  # print(colleges)
  # Print names and HTML of all colleges
  for college in colleges:
    print(college.text)
    print(college)
    parseSubjectsFromCollege(college)

def parseSubjectsFromCollege(collegesSoup):
  # This is currently broken. It looks like each college needs to be clicked to expand.
  # To do this, you may have to pass in the webdriver object, click the <a> element in
  # each college <div> element, and then create a new soup object from the new HTML.
  subjects = collegesSoup.findAll('a', id=re.compile('^LINK1\$\d+'))
  print(subjects)
  for subject in subjects:
    print(subject.text)

parse()
