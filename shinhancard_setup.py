#%% packages
import sys, time
sys.path.append('C:/Users/samsung/Desktop/Python_Jonginn/project/Cardcompany/common/url/')
sys.path.append('C:/Users/samsung/Desktop/Python_Jonginn/project/Cardcompany/common/save/')
sys.path.append('C:/Users/samsung/Desktop/Python_Jonginn/project/Cardcompany/common/browser/')
sys.path.append('C:/Users/samsung/Desktop/Python_Jonginn/project/Cardcompany/common/cardbox/')
sys.path.append('C:/Users/samsung/Desktop/Python_Jonginn/project/Cardcompany/common/benefitbox/')

from url_setup import Url
from save_setup import Save
from browser_setup import Browser
from cardbox_setup import CardBox
from benefitbox_setup import BenefitBox

#%%

class ShinhanUrl(Url):

    '''
    ============================================

    0) built-in attribute

    ============================================
    '''

    ############################################
    # overrided in a child class
    url_top = "https://www.shinhancard.com/pconts/html/card/main/main.html"

    xpath_url = """
    //div[@class='kategorie-type01']
    //li
    //a[@href and @role='button']
    """

    xpath_dict = {
        'type' : (
            """
            .//strong[@class='tit01']
            """
            , 'text'
        )
        , 'url' : (
            """
            .
            """
            , 'href'
        )
    }
    ############################################


class ShinhanSave(Save):

    root_pickle_path = "C:/Users/samsung/Desktop/Python_Jonginn/project/Cardcompany/Shinhancard/shinhancard_pickle/"


class ShinhanBrowser(Browser):

    pass


class ShinhanCardBox(CardBox):

    '''
    ============================================

    0) built-in attribute

    ============================================
    '''

    xpath_card_box = """
    //section[@class='contents']
    //div[@data-plugin-view='cmmCardList']
    //li[./div[contains(@class, 'card_img_wrap')]]
    """

    xpath_dict = {
        'href' : (
            """
            .//a[@href and @class='card_name' and @role='button']
            """
            , 'href'
        )
        , 'name' : (
            """
            .//a[@href and @class='card_name' and @role='button']
            """
            , 'text'
        )
    }


class ShinhanBenefitBox(BenefitBox):

    ############################################
    # overrided in a child class
    xpath_benefit_box_basic = """
    //div[@id='cardCompareAfter' and contains(@class, 'ly_inner')]
    """

    xpath_benefit_box_tab = """
    //div[contains(@class, 'tab_type01 swiper_tab card_detail_tab') and contains(@id, 'tabSwiper0')]
    """

    xpath_scroll_down = """
    //ul[@class='tab_list swiper-wrapper' and @role='tablist']
    """

    xpath_tab_initiate = """
    //ul[@class='tab_list swiper-wrapper' and @role='tablist']
    //li[a[@href and @role='tab' and @aria-selected and @class='role_link']][1]
    """

    xpath_tab_select = """
    //ul[@class='tab_list swiper-wrapper' and @role='tablist']
    //li[a[@href and @role='tab' and @aria-selected='true' and @class='role_link']]
    /following-sibling::li[a[@href and @role='tab' and @aria-selected and @class='role_link']][1]
    """

    xpath_dict_basic = {
        'name': (
            """
            .//div[contains(@class, 'card_detail')]
            //div[@class='card_name' and @data-plugin-html='cardNmArea']
            """
            , 'text'
        )
        , 'brand': (
            """
            .//div[contains(@class, 'card_accor_section')]
            //table[.//caption[contains(*, '연회비')]]
            //tbody//span[@class='ico_brand']/img[@src and @alt]
            """
            , 'alt'
        )
        , 'fee': (
            """
            .//div[contains(@class, 'card_accor_section')]
            //table[.//caption[contains(*, '연회비')]]
            //tbody//td[@class='wgt_md color_darkgray']
            """
            , 'text'
        )

        # , 'brand_fee_html': (
        #     """
        #     .//div[contains(@class, 'card_accor_section')]
        #     """
        #     , 'innerHTML'
        # )
    }

    xpath_dict_tab = {
        'tab_name': (
            """
            .//ul[@class='tab_list swiper-wrapper' and @role='tablist']
            //li[a[@href and @role='tab' and @aria-selected='true' and @class='role_link']]
            """
            , 'text'
        )
        , 'tab_contents': (
            """
            .//div[contains(@class, 'tab_wrap swiper-container swiper_tabCont')]
            //li[starts-with(@id, 'section') and contains(@class, 'swiper-slide tab_cont') and @role='tabpanel' and @aria-hidden='false']
            """
            , 'innerHTML'
        )
    }
    ############################################

