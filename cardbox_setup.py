#%% packages
import sys, time
sys.path.append('C:/Users/samsung/Desktop/Python_Jonginn/project/Cardcompany/common/box/')
from box_setup import Box


#%%

class CardBox(Box):

    '''
    ============================================

    0) built-in attribute

    ============================================
    '''

    # need to be overrided in a child class
    xpath_card_box = """

    """

    # need to be overrided in a child class
    xpath_dict = {}


    '''
    ============================================

    1) extract card box

    ============================================
    '''

    @classmethod
    def card_box_extract(cls, cb_elem, xpath_dict):
        '''
        #### parameters ####
        cb_elem    : card box                         , web element
        xpath_dict : key - xpath name                 , text
                     val - tuple of xpath & attribute , tuple (text/text)
        '''
        for name, tup in xpath_dict.items():
            yield {name: cls.box_detail_extract(cb_elem, tup[0], tup[1])}


    '''
    ============================================

    2) card box list             

    ============================================
    '''

    @classmethod
    def card_box_list(cls, driver, card_co, url):
        '''
        #### parameters ####
        driver            : selenium browser                 , driver object
        card_co           : target company                   , text
        url               : target url                       , text
        xpath_dict (class): key - xpath name                 , text
                            val - tuple of xpath & attribute , tuple (text/text)
        '''
        print(f'{card_co} : {url}')
        driver.get(url)
        time.sleep(5)

        for cb_elem in driver.find_elements_by_xpath(cls.xpath_card_box):
            tmp_dict = {'card_co': card_co, 'url': url}
            for dic_ in cls.card_box_extract(cb_elem, cls.xpath_dict):
                tmp_dict.update(dic_)
            yield tmp_dict
