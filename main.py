from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down_speed = None
        self.up_speed = None
        self.service = Service(executable_path="C:\Development\chromeself.driver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.promise_up = 100
        self.promise_down = 150

    def get_internet_speed(self):
        URL = "https://www.speedtest.net/"
        self.driver.get(url=URL)
        self.driver.maximize_window()
        time.sleep(2)
        go_btn = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_btn.click()

        time.sleep(45)

        self.down_speed = self.driver.find_element(By.XPATH,
                                         '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up_speed = self.driver.find_element(By.XPATH,
                                       '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        self.driver.quit()

    def tweet_at_provider(self):
        time.sleep(2)
        URL = "https://www.twitter.com"
        EMAIL = "engtesting23@gmail.com"
        PASSWORD = "**********"

        self.driver.get(url=URL)
        self.driver.maximize_window()
        time.sleep(4)

        login = self.driver.find_element(By.XPATH,
                                    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login.send_keys(EMAIL)

        time.sleep(2)
        login.send_keys(Keys.ENTER)

        time.sleep(4)

        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys("Mohit230802")

        time.sleep(2)
        username.send_keys(Keys.ENTER)

        time.sleep(3)

        password = self.driver.find_element(By.XPATH,
                                       '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = (f"Hey Internet Provider, why is my internet speed {self.down_speed}down/{self.up_speed}up when I pay for {self.promise_down}down/{self.promise_up}up?")
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

        input(Keys.ENTER)


Speed = InternetSpeedTwitterBot()
Speed.get_internet_speed()
Tweet = InternetSpeedTwitterBot()
Tweet.tweet_at_provider()
