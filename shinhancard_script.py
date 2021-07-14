#%% packages
import os, sys, time, datetime, pickle
import pandas as pd
sys.path.append('C:/Users/samsung/Desktop/Python_Jonginn/project/Cardcompany/Shinhancard/')

from shinhancard_setup import ShinhanUrl, ShinhanSave, ShinhanBrowser, ShinhanCardBox, ShinhanBenefitBox

# date = '20210702'
date = datetime.datetime.now().date().strftime("%Y%m%d")
card_co = '신한카드'
chrome_path = 'C:\\Users\\samsung\\Desktop\\ChromeDriver\\chromedriver'

#%% functions

def row_list_gen(generator):
    try:
        row_list = []
        for dict_ in generator:
            row_list.append(dict_)
        return row_list
    except:
        print('Something went wrong !')
        raise NameError('Need to be investigated !')
        

def main(url=True, card_box=True, benefit_box=True):
    print(f'''
    url : {url}
    card_box : {card_box}
    benefit_box : {benefit_box}
    ''')

    # # check boolean types
    # assert type(url) == bool
    # assert type(card_box) == bool
    # assert type(benefit_box) == bool

    # global variables
    global date
    global card_co
    global chrome_path


    # open a browser
    driver = ShinhanBrowser.browser_session(chrome_path)


    # collect urls
    file_name = f'url/{date}_shinhancard_url.pickle'
    if url:
        ## generator
        shinhancard_url_gen = ShinhanUrl.url_collect(
            driver=driver
            , card_co=card_co
        )

        ## execute a generator
        url_row_list = row_list_gen(shinhancard_url_gen)

        ## save a pickle file
        url_df = pd.DataFrame(data=url_row_list)
        ShinhanSave.pickle_save(url_row_list, file_name)
    else:
        ## get a recent pickle name
        dir_list = os.listdir(ShinhanSave.root_pickle_path + 'url/')
        dir_list = [i for i in dir_list if i.endswith('url.pickle')]
        dir_list.sort()

        ## open a pickle file
        try:
            url_df = ShinhanSave.pickle_open(file_name='url/' + dir_list[-1])
        except:
            raise NameError('No pickle files !')

    # collect card boxes
    if card_box:
        for i, row in url_df.iterrows():
            type = row['type']

            file_name = f'collection/{date}_shinhancard_{type}_card_box.pickle'
            ## generator
            shinhancard_card_box_gen = ShinhanCardBox.card_box_list(
                driver=driver
                , card_co=card_co
                , url=row['url']
            )

            ## execute a generator
            card_box_row_list = row_list_gen(shinhancard_card_box_gen)

            ## save a pickle file
            ShinhanSave.pickle_save(card_box_row_list, file_name)
    else:
        pass

    ## get a recent pickle name
    dir_list = os.listdir(ShinhanSave.root_pickle_path + 'collection/')
    dir_list = [i for i in dir_list if i.endswith('card_box.pickle')]
    dir_list.sort()
    dir_list = [i for i in dir_list if i.startswith(dir_list[-1][:8])]

    ## open and merge pickle files
    df_concat = []
    try:
        for dir_ in dir_list:
            tmp = ShinhanSave.pickle_open(file_name='collection/' + dir_)
            tmp['type'] = dir_.split('_')[2]
            df_concat.append(tmp.copy())
        card_box_df = pd.concat(df_concat, ignore_index=True)
    except:
        raise NameError('No pickle files !')


    # collect benefit boxes
    if benefit_box:
        try:
            benefit_box_row_list = []
            for i, row in card_box_df.iterrows():
                ## progress bar
                total_len = len(card_box_df)
                status = i*"#" + (total_len-i)*"-"
                print(f"\r{status} {i}%", end="")

                ## generator
                shinhancard_benefit_box_gen = ShinhanBenefitBox.benefit_box_list(
                    driver=driver
                    , card_co=card_co
                    , url=row['href']
                )

                ## execute a generator
                benefit_box_row_list.extend(row_list_gen(shinhancard_benefit_box_gen))
        finally:
            ## save a pickle file
            file_name = f'individual/{date}_shinhancard_benefit_box.pickle'
            ShinhanSave.pickle_save(benefit_box_row_list, file_name)
    else:
        pass

#%% execution

main(url=True, card_box=True, benefit_box=True)
