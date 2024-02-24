import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

months = ["January","February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
categories = ["Electric","Classic","Docked"]
monthValues = []

for month in months:

        df = pd.read_csv(f'{month}.csv')

        rideAbleType = df['rideable_type']

        #print(rideAbleType.unique())

        electric = 0
        classic = 0
        docked = 0
       

        for cell in rideAbleType:
                if cell == "electric_bike":
                        electric+=1
                elif cell == "classic_bike":
                        classic +=1
                elif cell == "docked_bike":
                        docked +=1
               

        monthValues.append((electric, classic, docked))
        print(f"In {month}: electric: {electric}, classic: {classic}, docked: {docked}")


# Setting the positions for the bars
pos = np.arange(len(categories))
n_categories = len(categories)
monthLength = len(months)
 # the width of the bars
# Plotting
width = 0.8 / len(months)
bar_width = 0.2
fig, ax = plt.subplots()

for i, (month, values) in enumerate(zip(months, monthValues)):
    # Calculate base position for the month
    month_pos = np.arange(len(months)) * (n_categories + 1) * bar_width
    
    # Offset positions for each category within the month
    for j, category in enumerate(categories):
        pos = month_pos[i] + (j * bar_width)
        ax.bar(pos, values[j], width=bar_width, label=category if i == 0 else "", color=plt.cm.tab10(j))
    
# Set x-ticks to be in the middle of each group of bars for each month
tick_positions = np.arange(len(months)) * (n_categories + 1) * bar_width + (bar_width * n_categories) / 2

ax.set_xticks(tick_positions)
ax.set_xticklabels(months)

# Add labels and title
plt.xlabel('Months')
plt.ylabel('Number of Bikes')
plt.title('Number of Bikes by Type Each Month')

# Add a legend
ax.legend(categories, title="Bike Type", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
