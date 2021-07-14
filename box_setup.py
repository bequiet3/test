#%%
class Box:

    '''
    ============================================

    0) text cleansing              

    ============================================
    '''

    @classmethod
    def text_cleansing(cls, text):
        '''
        #### parameters ####
        text : text, text
        '''
        return str(text).replace('\n', ' ').strip()


    '''
    ============================================

    1) box extract                

    ============================================
    '''

    @classmethod
    def box_detail_extract(cls, wb_elem, xpath, attr):
        '''
        #### parameters ####
        wb_elem : box,       web element
        xpath   : xpath,     text
        attr    : atrribute, web element
        '''
        if len(wb_elem.find_elements_by_xpath(xpath)) == 1:
            if attr == 'text':
                return str(wb_elem.find_element_by_xpath(xpath).text).strip()
            else:
                return str(wb_elem.find_element_by_xpath(xpath).get_attribute(attr)).strip()
        elif len(wb_elem.find_elements_by_xpath(xpath)) >= 2:
            if attr == 'text':
                # return '|'.join([str(i.text).replace('\n', ' ').strip() for i in wb_elem.find_elements_by_xpath(xpath)])
                return '|'.join([Box.text_cleansing(i.text) for i in wb_elem.find_elements_by_xpath(xpath)])
            else:
                # return '|'.join([str(i.get_attribute(attr)).replace('\n', ' ').strip() for i in wb_elem.find_elements_by_xpath(xpath)])
                return '|'.join([Box.text_cleansing(i.get_attribute(attr)) for i in wb_elem.find_elements_by_xpath(xpath)])
        else:
            return None
