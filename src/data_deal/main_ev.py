import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


size_mapping = {
    'Two-seater': 1,
    'Minicompact': 2,
    'Subcompact': 3,
    'Compact': 4,
    'Station wagon: Small': 5,
    'Sport utility vehicle: Small': 6,
    'Mid-size': 7,
    'Station wagon: Mid-size': 8,
    'Full-size': 9,
    'Sport utility vehicle: Standard': 10,
    'Minivan': 11,
    'Pickup truck: Standard': 12
}


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

def df_country_map(df:pd.DataFrame, map_csv_fl:str='data/ev_data_model_country.csv')->pd.DataFrame:
    '''
    Docstring for df_country_map
        this is to map the make vs its original country
    '''
    mdf = pd.read_csv(map_csv_fl)
    make, country = 'Make', 'Country'
    
    rel_df = mdf[[make, country]].copy()
    rel_df.drop_duplicates(inplace=True)
    rel_df.reset_index(drop = True, inplace=True)
    
    df_new = pd.merge(df, rel_df, how = 'left', left_on='Make', right_on='Make')
    return df_new
    
def about_num_data(fl_name:str):
    df = pd.read_csv(fl_name)
    df = df_country_map(df)
    
    # Apply to your dataframe, this is to transfer the vehicle class into some meaningful number/ encoding it. 
    df['Vehicle_Class_Numeric'] = df['Vehicle class'].map(size_mapping)
    v_class_num = 'Vehicle_Class_Numeric'
    country = 'Country'

    year = 'Model year'
    m_kw = 'Motor (kW)' # the power of the motor
    rech_t = 'Recharge time (h)'
    energy_eff = 'Energy Efficiency (km/kWh)' # with every unit of battery capacity, how much km can run. this is to check battery turn out efficiency, 
    spd = 'spd_km/h' # the max spd to run with the motor
    v_class = 'Vehicle class'
    df[spd] = df[energy_eff]*df[m_kw]
    rech_vs_power = 'recharge_vs_power' # the battery capacity should match to the power, so this parameter is to link the battery with the motor power
    df[rech_vs_power] = df[rech_t]/df[m_kw]
    
    
    # # this is to check the motor power vs charging hous/ power, with the vehicle class as the color shown
    # unique_classes = df[v_class].unique()
    # cm = plt.get_cmap('tab20')
    
    # for i, (name, group) in enumerate(df.groupby(v_class)):
    #     plt.scatter(x=group[m_kw], y=group[rech_vs_power], alpha=0.2, label=name, color=cm(i % 20))

    # plt.xlabel(f'{m_kw}')
    # plt.ylabel(f'{rech_vs_power}')
    # plt.legend(title=v_class, bbox_to_anchor=(1.05, 1), loc='upper left')
    # plt.tight_layout()
    # plt.show()
    
    # # this is to check the motor power vs recharging/power, and shown the year.
    # plt.scatter(x = df[m_kw], y = df[rech_vs_power], c = df[year], cmap = 'viridis', alpha = .2) # , c = df[year], cmap = 'viridis'
    # plt.xlabel(f'{m_kw}')
    # plt.ylabel(f'{rech_vs_power}')
    # plt.colorbar(label=year)
    # plt.show()
    
    # # this is to check the vehicle class vs m_kw
    # plt.scatter(x = df[m_kw], y = df[v_class_num], c = df[year], cmap= 'viridis', alpha = .2)
    # plt.colorbar(label = year)
    # plt.xlabel(f'{m_kw}')
    # plt.ylabel(f'{v_class_num}')
    # plt.show()
    # # this shows more vehicle types come out with the time goes
    
    '''
    STOP HERE
    '''
    # check the v_class vs motor power color / label is country
    
    unique_classes = df[country].unique()
    cm = plt.get_cmap('tab20')
    
    for i, (name, group) in enumerate(df.groupby(country)):
        plt.scatter(x=group[m_kw], y=group[v_class_num], alpha=0.2, label=name, color=cm(i % 20))

    plt.xlabel(f'{m_kw}')
    plt.ylabel(f'{v_class_num}')
    plt.legend(title=country, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    
    
    '''    
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
    
    # about_cat_data(csv_fl)
    about_num_data(csv_fl)