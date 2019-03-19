from mitmproxy import ctx
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--proxy-server=http://192.168.107.8:8080")
browser = webdriver.Chrome(chrome_options = chromeOptions)
browser.get("https://vhsupply.staging.viewchain.net")

    
ctx.log.info(flow.request.headers)  
