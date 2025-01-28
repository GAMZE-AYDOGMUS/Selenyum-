from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from time import sleep

class Ziraat():
    def __init__(self):
        self.tarayici=Firefox()
        self.siteye_git()
        self.clickler()
        self.sayfa_gecis()
    
    def siteye_git(self):
        self.tarayici.get("https://www.ziraatyatirim.com.tr/tr/sabah-stratejisi")
        sleep(2)

    def clickler(self):
        self.tarayici.find_element(By.XPATH,'/html/body/section/div[2]/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/label').click()
        sleep(1)
        self.tarayici.find_element(By.XPATH, "//*[@id=btnPdfFilter]").click()
        sleep(1)

    def sayfa_gecis(self):
        for i in range(1,204):
            self.tarayici.find_element(By.XPATH, f"//*[@id=pagesView]/a[{i}]").click()
        
t= Ziraat()

    