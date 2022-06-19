import pandas as pd

def read_data(path):
    return pd.read_json(path)

def calculate_bmi(df):
    '''
    This function calculates the BMI, the BMI Category as well as the Health Risk
    :param df: A dataframe containing patient data with columns: 'Gender','HeightCm','WeightCm'
    :return: A dataframe with 3 additional columns: BMI, BMI Category, Health Risk
    '''
    # Calculate the BMI
    df['BMI'] = df['WeightKg'] / (df['HeightCm'] / 100) ** 2

    # Calculate the BMI category
    df['BMI Category'] = pd.cut(df['BMI'], [0, 18.4, 24.9, 29.9, 34.9, 39.9, 200],
                                           labels=['Underweight', 'Normal weight', 'Overweight',
                                                   'Moderately obese', 'Severely obese', 'Very severely obese'])

    # Calculate the Health Risk
    df['Health Risk'] = pd.cut(df['BMI'], [0, 18.4, 24.9, 29.9, 34.9, 39.9, 200],
                                          labels=['Malnutrition risk', 'Low risk', 'Enhanced risk',
                                                  'Medium risk', 'High risk', 'Very high risk'])

    return df

def get_bmi_category_count(df,category='normal weight'):
    '''
    This function counts the number of patients that are in the given category
    :param df: A dataframe containing patient data with columns: 'Gender','HeightCm','WeightCm'
    :param category: String. A category. One of: ['Underweight', 'Normal weight', 'Overweight',
                                                   'Moderately obese', 'Severely obese', 'Very severely obese']
    :return:
    '''

    if category == 'normal':
        category = 'normal weight'
    elif category == 'over weight':
        category = 'overweight'

    categories = ['Underweight', 'Normal weight', 'Overweight',
                                                   'Moderately obese', 'Severely obese', 'Very severely obese']

    # Check if the given category is in the categories list and raise error if it isn't
    if category.lower() not in list(map(lambda x: x.lower(),categories)):
        raise Exception('The given category {} is not in one of {}'.format(category,categories))

    # Check if the BMI Category was calculated and if not calculate it
    if 'BMI Category' not in df.columns:
        df = calculate_bmi(df)

    return (df['BMI Category'].str.lower() == category.lower()).sum()
