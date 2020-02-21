from selenium import webdriver
from time import sleep
import random


class Typebot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def type(self):
        self.driver.get('https://10fastfingers.com/multiplayer')
        count = 0
        # wait 10 secs to load
        sleep(1)

        username = self.driver.find_element_by_xpath('//*[@id="username"]')

        username.click()

        username.send_keys('keg')

        usernameEnter = self.driver.find_element_by_xpath(
            '//*[@id="auth"]/input[2]')

        usernameEnter.click()

        sleep(10)

        # get the input box
        inputBox = self.driver.find_element_by_xpath(
            '//*[@id="game"]/div[3]/div[2]/div[2]/div[1]/input')
        inputBox.click()
        inputBox.clear()

        while True:

            # number generator to make mistakes on purpose
            num = random.randint(1, 30)

            # get highlighted word
            word = self.driver.find_element_by_class_name('highlight')

            # get timer
            #timer = self.driver.find_element_by_id('timer')

            if count == 20:
                print('times up')
                break
            try:
                sleep(.5)  # speed

                print(word.text)
                # print(timer.text)
                inputBox.send_keys(word.text)
                # makes a mistake if a random number between 1,40 is 5
                if num == 5:
                    inputBox.send_keys('t')

                inputBox.send_keys(" ")
                count += 1
            except Exception:
                print('there was a problem')
                break
        print('Done...')


bot = Typebot()

bot.type()
