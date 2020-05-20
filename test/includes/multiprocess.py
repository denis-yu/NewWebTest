from multiprocessing import Pool
import os, time, random
from selenium import webdriver
import sys
sys.path.append(os.getcwd())
# sys.path.append(os.getcwd()+"/MedicarePlanDetail.py")
# print(os.getcwd())

from MedicarePlanDetail import testMedicarePlanDetail



def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


class startBrowser():
    def __init__(self, browsername):
        # self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
        # self.driver = webdriver.Chrome(executable_path='../../driver/chromedriver')
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        print("start the browser..." + browsername)
        self.vars = {}

    def teardown_method(self, browsername):
        self.driver.quit()
        print("quit the browser..." + browsername)

    def test_medicare(self):
        # Test name: medicare
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://sunmaker.medicare.healthinsurance.com")
        # 2 | setWindowSize | 1440x900 |
        self.driver.set_window_size(1440, 900)


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(2)
    for i in range(2):
        p.apply_async(long_time_task, args=(i,))
        # b = startBrowser(str(i))
        c = testMedicarePlanDetail()
        c.setup_method("chrome")
        c.test_medicare()
        c.teardown_method("chrome")
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
