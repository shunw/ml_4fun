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

def about_cat_data(fl_name:str):
    df = pd.read_csv(fl_name)
    cat_cal = ['Make', 'Vehicle class']
    for c in cat_cal:
        print ()
        print (f'check {c}')
        print (sorted(df[c].unique()))
        print (len(df[c].unique()))

def about_num_data(fl_name:str):
    
    df = pd.read_csv(fl_name)
    year = 'Model year'
    m_kw = 'Motor (kW)'
    rech_t = 'Recharge time (h)'
    energy_eff = 'Energy Efficiency (km/kWh)'
    spd = 'spd_km/h'
    df[spd] = df[energy_eff]*df[m_kw]
    
    plt.scatter(x = df[spd], y = df[rech_t], alpha = .3, c = df[year], cmap = 'viridis')
    plt.xlabel(f'{spd}')
    plt.ylabel(f'{rech_t}')
    plt.colorbar(label=year)
    plt.show()
    '''
    checked with the year vs recharge_time. 
        - no strong relationship
    checked with spd vs recharge_time
        - some relationship. may also need to add year into there, to check if some higher spd but the recharging time is not higher
    what will be my purpose for this ev data? Since it has 
    ??? different countries car will have different efficiency? or charging time? --- previous we say that japan's car save the oil/ use the efficiency the most. Is now same thing? 
        if so, need to category the make with different countries.

    ??? recharge time usually reflect one company's attitude to its battery, will different maker's recharging time is also different? need to category with different model/ car size? 

    ??? will the make year -> different battery contribute to the car? 
        will this mean later year, the car will have more power?
        will this mean later year, the charging time will longer no matter about the car make? 
        
    data - visualization 
    ??? with the geography data, we also can see the trend that which country develop the more models? this 
    
    ??? or which model has the longest life time, which means people love it, so it cannot just end of life.
    
    '''

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='csv file to parse', required = True)
    
    args = parser.parse_args()
    csv_fl = args.file
    
    about_num_data(csv_fl)