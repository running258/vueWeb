import mitmproxy.http
from mitmproxy import ctx
from selenium import webdriver

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == "vhsupply.staging.viewchain.net":
            if "application/json" in flow.request.headers["accept"]:
                self.num = self.num + 1
                ctx.log.info("We've seen %d flows" % self.num)
                ctx.log.info("--------------------"+flow.request.host)
                ctx.log.info("--------------------"+flow.request.path)
                ctx.log.info("--------header------------"+flow.request.headers["accept"])
    
    

# https://vhsupply.staging.viewchain.net/#/login
   
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--proxy-server=http://127.0.0.1:8080")
browser = webdriver.Chrome(chrome_options = chromeOptions)


addons = [
    Counter()
]

