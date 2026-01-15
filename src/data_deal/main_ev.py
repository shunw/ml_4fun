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
    # scatter_matrix(df[num_col])
    df['Vehicle class'].hist(bins = 20)
    plt.show()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='csv file to parse', required = True)
    
    args = parser.parse_args()
    csv_fl = args.file
    
    rough_pic(csv_fl)