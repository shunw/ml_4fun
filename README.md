# this is for machine learning study

There are two datasets. One is from Kaggle's ev energy, and the other is from NASA dataset. 

Currently is a very beginning.

# ev energy

## thoughts about the data

### The most is Model, can these models be combined or not?

- the Answer is no: because with the same model, the creat year may be different, which means the battery or other performance of the car is also different. So, I will drop the model col and more forcus on the time and vehicle classes

### kW vs. kWh (Important Distinction) (from gemini)
- It is easy to confuse kW with kWh (kilowatt-hour) when looking at electric vehicles: 
  - kW (Power): Measures the motor's instantaneous strength (like the size of a water hose's flow).
  - kWh (Energy): Measures the battery capacity or "tank size" (like the total amount of water in a bucket). 


## data clean pipeline logic
- Need to clean the Make: remove the space from the name, and Smart EQ == Smart, So will remove the Smart EQ ther
- data split need to by Vehicle class

## need to check
- data correlation check
- study if the data combined, any interesting finding? 


# algae

Need to study how to deal with the mat data
