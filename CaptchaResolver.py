from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#Initialize Basic
url=r'http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do'

#initialize Webdriver
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cin_no="L17110MH1973PLC019786"
cin =driver.find_element_by_id("companyID")
cin.clear()
cin.send_keys(cin_no)

