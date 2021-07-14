#%% packages
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#%%

class Browser:
    
    '''
    ============================================

                0) browser option              

    ============================================
    '''

    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    @classmethod
    def add_options_arg(cls, opt):

        pass

    @classmethod
    def add_options_exp(cls, opt):

        pass


    '''
    ============================================

                1) browser session             

    ============================================
    '''

    @classmethod
    def browser_session(cls, chrome_path):
        driver = webdriver.Chrome(chrome_path, options=cls.options)
        time.sleep(5)
        return driver

