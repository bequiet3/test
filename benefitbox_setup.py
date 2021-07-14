#%% packages
import sys, time
sys.path.append('C:/Users/samsung/Desktop/Python_Jonginn/project/Cardcompany/common/box/')
from box_setup import Box

#%%

class BenefitBox(Box):
    
    '''
    ============================================

    0) built-in attribute

    ============================================
    '''

    ############################################
    # need to be overrided in a child class
    xpath_benefit_box_basic = """

    """

    xpath_benefit_box_tab = """

    """

    xpath_scoll_down = """
    
    """

    xpath_tab_initiate = """

    """

    xpath_tab_select = """

    """

    xpath_dict_basic = {}

    xpath_dict_tab = {}
    ############################################

    '''
    ============================================

    1) benefit box initialization & selection

    ============================================
    '''

    @classmethod
    def benefit_box_init_select(cls, driver, xpath):
        '''
        #### parameters ####
        driver : selenium browser , driver object
        xpath  : xpath            , text
        '''
        # tab click
        if len(driver.find_elements_by_xpath(xpath)) >= 1:
            driver.find_element_by_xpath(xpath).click()
            time.sleep(3)
            return True
        else:
            print('No tab exists !')
            return False


    '''
    ============================================

    2) scroll down to benefit box tab

    ============================================
    '''

    @classmethod
    def benefit_box_scroll_down(cls, driver, xpath):
        '''
        #### parameters ####
        driver : selenium browser , driver object
        xpath  : xpath            , text
        '''
        # tab click
        if len(driver.find_elements_by_xpath(xpath)) >= 1:
            # false -> scroll to bottom
            driver.execute_script("arguments[0].scrollIntoView(false);", driver.find_element_by_xpath(xpath))
            time.sleep(2)
        else:
            print('No tab exists !')

    '''
    ============================================

    3) benefit box extract                      

    ============================================
    '''

    @classmethod
    def benefit_box_extract(cls, bb_elem, xpath_dict):
        '''
        #### parameters ####
        bb_elem    : benefit box                      , web element
        xpath_dict : key - xpath name                 , text
                     val - tuple of xpath & attribute , tuple (text/text)
        '''
        for name, tup in xpath_dict.items():
            yield {name: cls.box_detail_extract(bb_elem, tup[0], tup[1])}


    '''
    ============================================

    4) benefit box extract loop

    ============================================
    '''

    @classmethod
    def benefit_box_extract_loop(cls, driver, bb_elem, result_dict, xpath_dict):
        '''
        #### parameters ####
        driver      : selenium browser                 , driver object
        bb_elem     : benefit box                      , web element
        result_dict : higher dictionary                , dict
        xpath_dict  : key - xpath name                 , text
                      val - tuple of xpath & attribute , tuple (text/text)
        '''
        break_ = True
        while break_:
            # extraction
            for dict_ in cls.benefit_box_extract(bb_elem, xpath_dict):
                result_dict.update(dict_)
            yield result_dict.copy()
            break_ = cls.benefit_box_init_select(driver, cls.xpath_tab_select)


    '''
    ============================================

    5) benefit box list

    ============================================
    '''

    @classmethod
    def benefit_box_list(cls, driver, card_co, url, tab=True):
        '''
        #### parameters ####
        driver     : selenium browser                 , driver object
        url        : target url                       , text
        card_co    : target company                   , text
        xpath_dict : key - xpath name                 , text
                     val - tuple of xpath & attribute , tuple (text/text)
        '''
        # access to a url
        # print(f'{card_co} : {url}')
        driver.get(url)
        time.sleep(5)

        # result dictionary initiation
        result_dict = {'card_co': card_co, 'url': url}

        #########################################################################
        # basic benefit box
        
        ## web element
        try:
            bb_elem = driver.find_element_by_xpath(cls.xpath_benefit_box_basic)
        except:
            print('No basic benefit box exists !')
            yield None

        ## extraction
        for dict_ in cls.benefit_box_extract(bb_elem, cls.xpath_dict_basic):
            result_dict.update(dict_)
        #########################################################################


        #############################################################################################
        # tab benefit box
        
        if tab:
            ## web element
            try:
                tb_elem = driver.find_element_by_xpath(cls.xpath_benefit_box_tab)
            except:
                print('No tab benefit box exists !')
                yield None

            ## scroll down
            cls.benefit_box_scroll_down(driver, cls.xpath_scroll_down)

            ## tab initialization
            cls.benefit_box_init_select(driver, cls.xpath_tab_initiate)
            time.sleep(1)

            ## extraciton
            for dict_ in cls.benefit_box_extract_loop(driver, tb_elem, result_dict, cls.xpath_dict_tab):
                yield dict_

        else:
            yield result_dict
        #############################################################################################
