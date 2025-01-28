from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from time import sleep

class Instagram():
    def __init__(self):
        self.tarayici=Firefox()
        self.siteye_git()
        self.form_doldur()

    def siteye_git(self):
        self.tarayici.get("https://www.instagram.com/accounts/login/")
        sleep(4)

    def form_doldur():
        Self.tarayici.find_element(By.CSS_SELECTOR, "")