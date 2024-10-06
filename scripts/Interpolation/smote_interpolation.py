import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
import warnings
import smogn

warnings.filterwarnings('ignore')


def smote_interpolation():

    data1 = pd.read_csv('data/unsampled/Unsampled_Analyte1.csv')
    data1 = data1.drop(['Unnamed: 0'], axis=1)
    data1['log'] = np.log(data1['CFU/mL'])


    data2 = pd.read_csv('data/unsampled/Unsampled_Analyte2.csv')
    data2 = data2.drop(['Unnamed: 0'], axis=1)
    data2['log'] = np.log(data2['CFU/mL'])


    data3 = pd.read_csv('data/unsampled/Unsampled_Analyte3.csv')
    data3 = data3.drop(['Unnamed: 0'], axis=1)
    data3['log'] = np.log(data3['CFU/mL'])


    ''' APPLYING SMOTE '''

    ext_data1 = data1.copy()

    for i in range(5):
        smogn_sensor = smogn.smoter(
            data = data1, 
            y = "CFU/mL",
            under_samp=False,
            drop_na_col=True,
            drop_na_row=True,
            samp_method="extreme",
            k = 5
        )
        ext_data1 = pd.concat([ext_data1, smogn_sensor])
        ext_data1 = ext_data1.reset_index(drop=True)
        print(len(ext_data1))
        

    ext_data2 = data2.copy()

    for i in range(5):
        smogn_sensor = smogn.smoter(
            data = data2, 
            y = "CFU/mL",
            under_samp=False,
            drop_na_col=True,
            drop_na_row=True,
            samp_method="extreme",
            k = 5
        )
        ext_data2 = pd.concat([ext_data2, smogn_sensor])
        ext_data2 = ext_data2.reset_index(drop=True)
        print(len(ext_data2))
        

    ext_data3 = data3.copy()

    for i in range(5):
        smogn_sensor = smogn.smoter(
            data = data3, 
            y = "CFU/mL",
            under_samp=False,
            drop_na_col=True,
            drop_na_row=True,
            samp_method="extreme",
            k = 5
        )
        ext_data3 = pd.concat([ext_data3, smogn_sensor])
        ext_data3 = ext_data3.reset_index(drop=True)
        print(len(ext_data3))
        

    ext_data1.to_csv('data/smote/Analyte1.csv', index=False)
    ext_data2.to_csv('data/smote/Analyte2.csv', index=False)
    ext_data3.to_csv('data/smote/Analyte3.csv', index=False)

if __name__ == '__main__':
    smote_interpolation()
    print('SMOTE interpolation complete')