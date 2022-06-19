import json
import pandas as pd
import numpy as np
from generate_data import generate_data
from BMI_Calculator import calculate_bmi,get_bmi_category_count

data_1 = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

data_2 = [{"Gender": "Male", "HeightCm": 100, "WeightKg": 24.9 },
{ "Gender": "Male", "HeightCm": 100, "WeightKg": 24.9 },
{ "Gender": "Male", "HeightCm": 100, "WeightKg": 18.5 },
{ "Gender": "Female", "HeightCm": 100, "WeightKg": 24.9},
{"Gender": "Female", "HeightCm": 100, "WeightKg": 24.9},
{"Gender": "Female", "HeightCm": 100, "WeightKg": 18.5}]

def unit_test_1():
    '''
    This unit test tests basic functionality
    :return: None
    '''
    print('Unit Test 1...')
    # Convert to a json object
    json_data = json.dumps(data_1)

    # Read the data into a dataframe
    df_parameters = pd.read_json(json_data)

    # Calculate BMI
    df_parameters = calculate_bmi(df_parameters)

    # Test the calculate bmi function
    expected = [32.83061455,32.79194476,23.7654321,22.4996371,31.11111111,29.4022733]
    expected = list(map(lambda x: np.round(x,3),expected))

    actual = df_parameters['BMI'].values
    actual = list(map(lambda x: np.round(x, 3), actual))

    assert np.array_equal(actual,expected), 'calculate_bmi is incorrectly calculating the bmi'


    # Test the get_bmi_category_count function
    ls_categories = ['underweight', 'normal weight', 'Overweight', 'moderately obese', 'severely obese',
                     'very severely obese']
    ls_expected = [0, 2, 1, 3, 0, 0]

    for expected,category in zip(ls_expected,ls_categories):
        actual = get_bmi_category_count(df_parameters,category)

        assert np.array_equal(actual, expected), 'get_bmi_category_count has gotten the wrong number of {}\nExpected={},Actual={}'.format(category,expected,actual)

    print('Unit Test 1 Passed!')

def unit_test_2():
    '''
    This unit test checks bulk read functionality.
    :return: None
    '''

    print('Unit Test 2...')
    # Generate random data
    generate_data(1000000,seed=12345)

    # Read the data that was just generated
    df_parameters = pd.read_json('health_parameters.json')

    # Calculate BMI
    df_parameters = calculate_bmi(df_parameters)

    expected = np.round(27.131948571696103,3)
    actual = np.round(df_parameters['BMI'].mean(),3)

    assert expected == actual, 'Error in calculate_bmi. Mean BMI is expected to be {} but was {}'.format(expected,actual)

    expected = 'Overweight'
    actual = df_parameters['BMI Category'].mode()[0]

    assert expected == actual, 'Error in calculate_bmi. The most occurring category should be {} but it is {}'.format(expected,
                                                                                                         actual)

    print('Unit Test 2 Passed!')

def unit_test_3():
    '''
    This unit test tests edge cases
    :return: None
    '''
    print('Unit Test 3...')
    # Convert to a json object
    json_data = json.dumps(data_2)

    # Read the data into a dataframe
    df_parameters = pd.read_json(json_data)

    # Calculate BMI
    df_parameters = calculate_bmi(df_parameters)

    # Test the calculate bmi function
    expected = [24.9, 24.9, 18.5, 24.9, 24.9, 18.5]
    expected = list(map(lambda x: np.round(x,3),expected))

    actual = df_parameters['BMI'].values
    actual = list(map(lambda x: np.round(x, 3), actual))

    assert np.array_equal(actual,expected), 'calculate_bmi is incorrectly calculating the bmi'


    # Test the get_bmi_category_count function
    ls_categories = ['underweight', 'normal weight', 'Overweight', 'moderately obese', 'severely obese',
                     'very severely obese']
    ls_expected = [0, 6, 0, 0, 0, 0]

    for expected,category in zip(ls_expected,ls_categories):
        actual = get_bmi_category_count(df_parameters,category)

        assert np.array_equal(actual, expected), 'get_bmi_category_count has gotten the wrong number of {}\nExpected={},Actual={}'.format(category,expected,actual)

    print('Unit Test 3 Passed!')

if __name__ == '__main__':
    unit_test_1()
    unit_test_2()
    unit_test_3()