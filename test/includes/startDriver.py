from selenium import webdriver
import time


class startDriver():
    def setup_method(self):
        # self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome(executable_path='../../driver/chromedriver')
        self.driver = webdriver.Chrome()
        print("start the browser...")
        self.vars = {}
        return self.driver

    def teardown_method(self):
        self.driver.quit()
        print("quit the browser...")


if __name__ == '__main__':
    newtest = startDriver()
    # newTest.__init__("chrome")
    time.sleep(10)
    newtest.teardown_method()
