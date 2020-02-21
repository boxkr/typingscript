from selenium import webdriver
from time import sleep
import random


class Typebot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def type(self):
        self.driver.get('https://10fastfingers.com/typing-test/english')

        # wait 10 secs to load
        sleep(5)

        # get the input box
        inputBox = self.driver.find_element_by_id('inputfield')
        inputBox.click()
        inputBox.clear()

        while True:

            # number generator to make mistakes on purpose
            num = random.randint(1, 30)

            # get highlighted word
            word = self.driver.find_element_by_class_name('highlight')

            # get timer
            timer = self.driver.find_element_by_id('timer')

            if timer.text == '0:01':
                print('times up')
                break
            try:
                sleep(.05)  # speed

                print(word.text)
                # print(timer.text)
                inputBox.send_keys(word.text)
                # makes a mistake if a random number between 1,40 is 5
                if num == 5:
                    inputBox.send_keys('t')

                inputBox.send_keys(" ")
            except Exception:
                print('there was a problem')
                break
        print('Done...')


bot = Typebot()

bot.type()
