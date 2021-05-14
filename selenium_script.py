import time
from selenium import webdriver

urls = []
with open('urls.txt', 'r') as f:
    for line in f:
        urls.append(line)
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
           'savefile.default_directory': '/Users/jeffshum/Dev/webscreenshot-frb/webpages/'}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')

for url in urls:
    driver = webdriver.Chrome(options=chrome_options)
    #driver.implicitly_wait(10)
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    #driver.execute_script('document.title="{}";'.format('url'));
    driver.execute_script('window.print();')
driver.quit()
