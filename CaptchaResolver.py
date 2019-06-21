from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from PIL import Image
import pytesseract
import subprocess as sp

def Resolve(path):
    print("Resampling the Image")
    sp.getstatusoutput("convert "+path+" -resample 600 "+path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    return pytesseract.image_to_string(Image.open(path))

def DownloadImage(driver):
    with open('tempfile.png', 'wb') as file:
        file.write(driver.find_element_by_id("captcha").screenshot_as_png)
    
def StartWeb(url):
    #initialize Webdriver
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    #Type Cin
    cin_no="L17110MH1973PLC019786"
    cin =driver.find_element_by_id("companyID")
    cin.clear()
    cin.send_keys(cin_no)

    #Download Captcha
    DownloadImage(driver)

    #ResolveCaptcha
    captcha_text='{}'.format(Resolve('tempfile.png'))
    print("Extracted text",captcha_text)

    cp =driver.find_element_by_id("userEnteredCaptcha")
    cp.clear()
    cp.send_keys(captcha_text)
    
    #press enter key
    cp.send_keys(Keys.ENTER)

#Initialize Basic
url=r'http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do'
StartWeb(url)
