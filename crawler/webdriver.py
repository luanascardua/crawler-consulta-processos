from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


start_urls = {
    'Alagoas': [
        'https://www2.tjal.jus.br/cpopg/open.do',
        'https://www2.tjal.jus.br/cposg5/open.do'
    ],
    'Ceará': [
        'https://esaj.tjce.jus.br/cpopg/open.do',
        'https://esaj.tjce.jus.br/cposg5/open.do'
    ]
}

def get_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--log-level=3')
    # chrome_options.add_argument('--headless')

    chrome = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome, options=chrome_options)

    return driver

driver = get_chrome_driver()