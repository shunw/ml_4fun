import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


def rough_pic(fl_name:str):
    df = pd.read_csv(fl_name)
    # print (df.info())
    # print (df.describe())
    a = df.groupby(['Make', 'Vehicle class'])['Model'].count()
    print (sorted(df['Vehicle class'].unique()))
    print (df.columns)
    num_col = ['Model year', 'Motor (kW)', 'Recharge time (h)', 'Energy Efficiency (km/kWh)']
    cat_cal = ['Make', 'Model', 'Vehicle class']
    # scatter_matrix(df[num_col])
    df['Vehicle class'].hist(bins = 20)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def learn_about_evdata(fl_name:str):
    df = pd.read_csv(fl_name)
    cat_cal = ['Make', 'Model', 'Vehicle class']
    for c in cat_cal:
        print ()
        print (f'check {c}')
        print (sorted(df[c].unique()))
        print (len(df[c].unique()))
    '''
    The most is Model, need to figure out if these models can be combined or not
        if these can be combined, need to deal with it. --- to check how to combine it. This should be one feature clining to the ev car field
    '''

    '''
    what will be my purpose for this ev data? Since it has 
    ??? different countries car will have different efficiency? or charging time? --- previous we say that japan's car save the oil/ use the efficiency the most. Is now same thing? 
        if so, need to category the make with different countries.

    ??? recharge time usually reflect one company's attitude to its battery, will different maker's recharging time is also different? need to category with different model/ car size? 

    ??? will the make year -> different battery contribute to the car? 
        will this mean later year, the car will have more power?
        will this mean later year, the charging time will longer no matter about the car make? 
    '''

if __name__ == '__main__':
    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-f', '--file', help='csv file to parse', required = True)
    
    # args = parser.parse_args()
    # csv_fl = args.file
    csv_fl = 'data/ev_data.csv'
    rough_pic(csv_fl)
    learn_about_evdata(csv_fl)
