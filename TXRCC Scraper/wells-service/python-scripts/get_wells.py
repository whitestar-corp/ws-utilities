import time, os, tempfile, sys, zipfile, io
from selenium import webdriver
from datetime import date, timedelta
from selenium.webdriver.support.ui import WebDriverWait

dr = r"D:\Users\rwhite\Downloads"
files = os.listdir(dr)
old_pipe_data = [file for file in files if file.startswith("documents")]
for file in old_pipe_data:
    path_to_file = os.path.join(dr, file)
    os.remove(path_to_file)

url = 'https://mft.rrc.texas.gov/link/'
page = ['4e9023eb-e4ee-45b8-81b7-aec1494c1e8e']
executable_path = r'D:\Users\rwhite\Downloads\chromedriver.exe'
element = ['//*[@id="fileTable:j_id__v_1"]/option[4]',
           '//*[@id="fileTable:j_id_1q"]/div/div[2]',
           '//*[@id="j_id_3a:j_id_3a"]/span']
targetdir = r'D:\Users\rwhite\Documents\texas-wells\wells-service\data\wells'

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
        """)

def extract(filepath, targetdir):
    z = zipfile.ZipFile(filepath)
    for f in z.namelist():
        dirname = os.path.splitext(f)[0]  
        content = io.BytesIO(z.read(f))
        zip_file = zipfile.ZipFile(content)
        for i in zip_file.namelist():
            zip_file.extract(i, targetdir)

def scrapeRRC(page=page, element=element, executable_path=executable_path):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path, options=options)
    driver.get(url + page[0])
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(element[0]).click()
    time.sleep(4)
    driver.find_element_by_xpath(element[1]).click()
    time.sleep(4)
    driver.find_element_by_xpath(element[2]).click()
    try:
        paths = WebDriverWait(driver, 10800).until(every_downloads_chrome)
    finally:
        driver.quit()
    return paths[0][8:]

if __name__ == '__main__':
    
    path = scrapeRRC()
    extract(path, targetdir)
