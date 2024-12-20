import pandas as pd
import numpy as np


def exponential_interpolation():


    def generate_interpolated_data(start, end, num_points):
        return np.linspace(start, end, num_points + 2)[1:-1] 

    input_file = "data/unsampled/Unsampled_Analyte1.csv"
    df = pd.read_csv(input_file)
    all_interpolated_data = {col: [] for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']}

    for index in range(len(df) - 1):  
        num_points = 2 ** (9 - index) 
        for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']:
            start = df.iloc[index][col]    
            end = df.iloc[index + 1][col]   
            interpolated_values = generate_interpolated_data(start, end, num_points)
            all_interpolated_data[col].extend(interpolated_values)

    interpolated_df1 = pd.DataFrame(all_interpolated_data)
    interpolated_df1.to_csv('data/exponential/Exponential_Analyte1.csv', index=False)


    input_file = "data/unsampled/Unsampled_Analyte2.csv"
    df = pd.read_csv(input_file)
    all_interpolated_data = {col: [] for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']}

    for index in range(len(df) - 1):  
        num_points = 2 ** (9 - index)  
        for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']:
            start = df.iloc[index][col]    
            end = df.iloc[index + 1][col] 
            interpolated_values = generate_interpolated_data(start, end, num_points)
            all_interpolated_data[col].extend(interpolated_values)


    interpolated_df2 = pd.DataFrame(all_interpolated_data)
    interpolated_df2.to_csv('data/exponential/Exponential_Analyte2.csv', index=False)



    input_file = "data/unsampled/Unsampled_Analyte3.csv"
    df = pd.read_csv(input_file)
    all_interpolated_data = {col: [] for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']}

    for index in range(len(df) - 1):  
        num_points = 2 ** (9 - index)  
        for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']:
            start = df.iloc[index][col]   
            end = df.iloc[index + 1][col]  
            interpolated_values = generate_interpolated_data(start, end, num_points)
            all_interpolated_data[col].extend(interpolated_values)

    interpolated_df3 = pd.DataFrame(all_interpolated_data)
    interpolated_df3.to_csv('data/exponential/Exponential_Analyte3.csv', index=False)

    interpolated_df1['Label'] = 1
    interpolated_df2['Label'] = 2
    interpolated_df3['Label'] = 3
    full_expo_data = pd.concat([interpolated_df1, interpolated_df2, interpolated_df3], axis=0)
    full_expo_data.to_csv('data/exponential/Exponential_labelled.csv', index=False)


if __name__ == '__main__':
    exponential_interpolation()
    print('Exponential Interpolation complete')