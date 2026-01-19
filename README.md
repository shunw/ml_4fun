# this is for machine learning study

There are two datasets. One is from Kaggle's ev energy, and the other is from NASA dataset. 

Currently is a very beginning.

# ev energy

## data clean pipeline logic
- Need to clean the Make: remove the space from the name, and Smart EQ == Smart, So will remove the Smart EQ ther
- data split need to by Vehicle class

## need to check
- data correlation check
- study if the data combined, any interesting finding? 


# algae

Gemini helps to create convert the mat file into readable dataframe. 
The algae.mat file has been successfully converted to a dataframe based on the format described in GEMINI.md.

  I created a process_algae_data function in src/data_deal/mat_data.py which:
   1. Loads the .mat file using scipy.io with struct_as_record=False.
   2. Iterates through the 3 raceway structures.
   3. Extracts each parameter (like pH, irradiance, etc.) that has data and time_num fields.
   4. Combines them into a "Long Format" DataFrame with columns: raceway, parameter, time_days, value.

  This format is robust for handling different sampling times (time_num) for different sensors.
