#%% packages
import sys, time
sys.path.append('C:/Users/samsung/Desktop/Python_Jonginn/project/Cardcompany/common/box/')
from box_setup import Box

#%%

class Url(Box):

    '''
    ============================================

    0) built-in attribute

    ============================================
    '''

    # need to be overrided in a child class
    url_top = ""

    # need to be overrided in a child class
    xpath_url = ""

    # need to be overrided in a child class
    xpath_dict = {}


    '''
    ============================================

    1) extract a url

    ============================================
    '''

    @classmethod
    def url_box_extract(cls, url_elem, xpath_dict):
        '''
        #### parameters ####
        url_elem   : card box                         , web element
        xpath_dict : key - xpath name                 , text
                     val - tuple of xpath & attribute , tuple (text/text)
        '''
        for name, tup in xpath_dict.items():
            yield {name: cls.box_detail_extract(url_elem, tup[0], tup[1])}


    '''
    ============================================

    2) collect urls

    ============================================
    '''

    @classmethod
    def url_collect(cls, driver, card_co):
        '''
        #### parameters ####
        driver             : selenium browser                 , driver object
        card_co            : target company                   , text
        url_top    (class) : card company url                 , text
        xpath_url  (class) : xpath of card-type url           , text
        xpath_dict (class) : key - xpath name                 , text
                             val - tuple of xpath & attribute , tuple (text/text)
        '''
        print(f'{card_co} : {cls.url_top}')
        driver.get(cls.url_top)
        time.sleep(5)

        for url_elem in driver.find_elements_by_xpath(cls.xpath_url):
            tmp_dict = {'card_co': card_co, 'url_top': cls.url_top}
            for dic_ in cls.url_box_extract(url_elem, cls.xpath_dict):
                tmp_dict.update(dic_)
            yield tmp_dict


