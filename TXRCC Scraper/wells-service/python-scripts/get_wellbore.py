import time, os, tempfile, sys, gzip, shutil
from selenium import webdriver
from datetime import date, timedelta
from selenium.webdriver.support.ui import WebDriverWait

dr = r"D:\Users\rwhite\Downloads"
file = 'dbf900.txt.gz'
path_to_file = os.path.join(dr, file)
if os.path.exists(path_to_file):
    os.remove(path_to_file)

url = 'https://mft.rrc.texas.gov/link/'
page = ['9ef1955f-cf26-4bd4-8030-1253eb772cf9']
executable_path = r'D:\Users\rwhite\Downloads\chromedriver.exe'
element = ['dbf900.txt.gz']

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
    with open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\dbf900_junk.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


with open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\dbf900_junk.txt', 'r') as infile, \
open(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\dbf900.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace('|', ' ')
    outfile.write(data)

os.remove(r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wellbore\dbf900_junk.txt')
