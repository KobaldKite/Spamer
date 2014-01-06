__author__ = 'Serge'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class flooder:
    def __init__(self):
        self.browser = webdriver.Firefox()

    def openPage(self, string):
        self.browser.get(string)

    def setWait(self, wait):
        self.browser.implicitly_wait(wait)

    def loginSparkle(self):
        loginButton = self.browser.find_element_by_xpath(u'//*[@id="min-width"]/body/table/tbody/tr/td/table[2]/tbody/tr/td/a[8]')
        loginButton.click()

        loginField = self.browser.find_element_by_name('username')
        passwordField = self.browser.find_element_by_name('password')
        submitButton = self.browser.find_element_by_class_name('mainoption')

        loginField.send_keys('Sparkle')
        passwordField.send_keys('no')
        submitButton.click()

    def loginChatBox(self):
        chatBox = self.browser.find_element_by_id('frame_chatbox')
        self.browser.switch_to_frame(chatBox)
        loginRef = self.browser.find_element_by_xpath(u'//*[@id="chatbox_main_options"]/a[2]')
        loginRef.click()
        self.browser.switch_to_default_content()

    def writeInChatBox(self):
        chatBox = self.browser.find_element_by_id('frame_chatbox')
        self.browser.switch_to_frame(chatBox)
        chatField = self.browser.find_element_by_xpath(u'//*[@id="chatbox_messenger_form"]/table/tbody/tr/td/table/tbody/tr/td[9]/span')
        chatField.click()
        messageField = self.browser.find_element_by_id('message')
        colorFactor = 0
        increase = 1
        while 1:
            if colorFactor > 4:
                increase = 0
            else:
                if colorFactor < 1:
                    increase = 1
            if increase:
                colorFactor += 1
            else:
                colorFactor -= 1
            messageField.send_keys(('[color=#{red}{green}{blue}]Hey![/color]'.format(red=hex(50), green=hex(220-40*colorFactor), blue=hex(30+40*colorFactor))).replace('0x', ''))
            messageField.send_keys(Keys.RETURN)
            time.sleep(3)
        self.browser.switch_to_default_content()


def doEverything():
    floodMachine = flooder()
    floodMachine.openPage('http://livethemagic.forumotion.org/')
    floodMachine.loginSparkle()
    floodMachine.loginChatBox()
    time.sleep(5)
    floodMachine.writeInChatBox()


if __name__ == '__main__':
    doEverything()
