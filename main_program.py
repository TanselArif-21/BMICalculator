import argparse
import BMI_Calculator
import os
import numpy as np
import generate_data

directory_path = os.path.join(os.getcwd(),'health_parameters_output.json')

parser = argparse.ArgumentParser()
parser.add_argument('-loadpath', '--loadpath',
                    required=False,
                    dest='loadpath',
                    help='Path to the json file',
                    type=str
                    )
parser.add_argument('-savepath', '--savepath',
                    required=False,
                    dest='savepath',
                    help='The file path to save the resulting file',
                    type=str
                    )
parser.add_argument('-savefiletype', '--savefiletype',
                    required=False,
                    dest='savefiletype',
                    help='Optional. The file type to save as csv or json(default)',
                    type=str
                    )
parser.add_argument('-category', '--category',
                    required=False,
                    dest='category',
                    help='Optional. The BMI Category you are interested in',
                    type=str
                    )
parser.add_argument('-generatedatasize', '--generatedatasize',
                    required=False,
                    dest='generatedatasize',
                    help='Optional. Generate random population data. Give the number of people to generate for',
                    type=int
                    )
args = parser.parse_args()

if args.generatedatasize is not None:
    generate_data.generate_data(args.generatedatasize)

loadpath = None
if args.loadpath is not None:
    loadpath = args.loadpath

category = None
if args.category is not None:
    category = args.category

savepath = directory_path
if args.savepath is not None:
    savepath = args.savepath

filetype = None
if args.savefiletype is not None:
    filetype = args.savefiletype

generatedatasize = None
if args.generatedatasize is not None:
    generatedatasize = args.generatedatasize

if loadpath is not None:
    df_parameters = BMI_Calculator.read_data(loadpath)

    if category is not None:
        n = BMI_Calculator.get_bmi_category_count(df_parameters,category)
        print('The number of patients in category {} is {}. This is {}% of the total population.'.format(category,n,np.round(n*100/len(df_parameters),2)))

    df_parameters = BMI_Calculator.calculate_bmi(df_parameters)

    if filetype is not None:
        if filetype.lower() == 'csv':
            savepath = savepath.replace('.json', '.csv')
            if 'csv' not in savepath:
                savepath = savepath + '.csv'
            df_parameters.to_csv(savepath)
        else:
            df_parameters.to_json(savepath)
    else:
        df_parameters.to_json(savepath)

    print('File saved to location {}'.format(savepath))
