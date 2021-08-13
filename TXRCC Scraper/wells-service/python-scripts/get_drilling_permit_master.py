import time, os, tempfile, sys, gzip, shutil
from selenium import webdriver
from datetime import date, timedelta
from selenium.webdriver.support.ui import WebDriverWait

dr = r"D:\Users\rwhite\Downloads"
file = 'daf804.txt.gz'
path_to_file = os.path.join(dr, file)
if os.path.exists(path_to_file):
    os.remove(path_to_file)

url = 'https://mft.rrc.texas.gov/link/'
page = ['91a36fea-4dad-4f26-96c3-30843d0e0315']
executable_path = r'D:\Users\rwhite\Downloads\chromedriver.exe'
element = ['daf804.txt.gz']

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
        """)

def scrapeRRC(page=page, element=element, executable_path=executable_path):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path, options=options)
    driver.get(url + page[0])
    driver.implicitly_wait(5)      
    driver.find_element_by_link_text(element[0]).click()
    try:
        paths = WebDriverWait(driver, 10800).until(every_downloads_chrome)
        print(paths)
    finally:
        driver.quit()

if __name__ == '__main__':
    
    scrapeRRC()

with gzip.open(path_to_file, 'rb') as f_in:
    with open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\drilling-permit\daf804.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
