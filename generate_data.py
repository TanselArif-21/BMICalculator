import pandas as pd
import numpy as np

def generate_data(size,save=True,seed=None):
    '''
    This function generates health data. Given a size, half will be male and the other half female
    :param size: Int. Number of patients
    :param save: Bool. If True it will save locally to a json file called health_parameters.json
    :return: If save is True, this function will not return anything. If save is False it will return a dataframe
    '''

    if seed is not None:
        np.random.seed(seed)

    men_height = np.random.randn(int(size/2))*7+176
    women_height = np.random.randn(int(size/2))*7+162
    men_gender = ['Male']*int(size/2)
    women_gender = ['Female']*int(size/2)
    men_wt = np.random.randn(int(size/2))*5+83.9
    women_wt = np.random.randn(int(size/2))*5+70.6

    height = np.concatenate([men_height,women_height])
    gender = np.concatenate([men_gender,women_gender])
    weight = np.concatenate([men_wt,women_wt])

    df = pd.concat([pd.Series(gender),pd.Series(height),pd.Series(weight)],axis=1)
    df.columns = ['Gender','HeightCm','WeightKg']

    if save:
        df.to_json('health_parameters.json')
    else:
        return df
