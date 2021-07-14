#%% packages
import pickle
import pandas as pd

#%%

class Save:

    '''
    ============================================

    0) built-in attribute

    ============================================
    '''

    # need to be overrided in a child class
    root_pickle_path = ""


    '''
    ============================================

    1) save as a pickle

    ============================================
    '''

    @classmethod
    def pickle_save(cls, list_dict, file_name):
        pd.DataFrame(data=list_dict).to_pickle(cls.root_pickle_path + file_name)
        print('A pickle file was saved.')

    @classmethod
    def pickle_open(cls, file_name):
        with open(cls.root_pickle_path + file_name, 'rb') as f:
            tmp = pickle.load(f)
        return tmp
