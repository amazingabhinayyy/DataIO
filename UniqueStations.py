import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

months = ["January","February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthValues = set()

for month in months:

        df = pd.read_csv(f'{month}.csv')

        rideAbleType = df['start_station_name']

        # Convert the unique numpy array to a list and then add each item to the set
        unique_types = rideAbleType.unique().tolist()
        monthValues.update(unique_types)  # Using update to add elements from the list to the set

# If you need to inspect the result
print(monthValues)


'''

Clark Street and Elm Street
DuSable Lake Shore Dr and Monroe Street
DuSable Lake Shore Dr and North Blvd
Kingsbury Street and Kinzie Street 
Michigan Avenue and Oak Street 
Millenium Park
Streeter Drive and Grand Avenue 
Theater on the Lake
Wells Street and Concord Lane
Wells Street and Elm Street

'''