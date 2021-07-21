import time
from selenium import webdriver
import json
import re

with open('urls.txt', 'r') as f:
    lines = f.read()
    urls = re.findall('(https://.*?.html)', lines) # https://stackoverflow.com/a/50977427/13767695
appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local",
            "account": ""
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState),
           'savefile.default_directory': './webpages/'}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=chrome_options)

def save_screenshot(url):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.get(url)
    #TODO: Click all elements: class="expander__trigger"
    expanders = driver.find_elements_by_class_name("expander__trigger")
    for expander in expanders:
        expander.click()
    time.sleep(5) # waiting for page to load after clicking expander buttons
    # Ref: https://stackoverflow.com/a/52572919/
    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    # driver.save_screenshot(path)  # has scrollbar
    title = " ".join(driver.title.replace("|",'').split())
    driver.find_element_by_tag_name('body').screenshot(f'./webpage_screenshots_2021.07.21/{title}.png')  # avoids scrollbar
    driver.set_window_size(original_size['width'], original_size['height'])
    #TODO: remove pipes from titles then save

if __name__ == '__main__':
    for url in urls:
        save_screenshot(url)

driver.quit()
