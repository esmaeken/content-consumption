import pandas as pd
import matplotlib.pyplot as plt

pd.read_csv('content_consumption_2023.csv')

csp = pd.read_csv('content_consumption_2023.csv')

from datetime import datetime

csp = 'content_consumption_2023.csv'

hour_counts = {}                      #dictionary to analyse csp for every hour 

with open(csp, 'r') as file:          #opening a file in read mode      #with statement to close a file after using
    reader = csv.reader(file)         
    next(reader)                       #to skip the header
    
    for row in reader:                #loop goes through every line
        dateandtime = row[6]
        if dateandtime:
            dateandtime1 = datetime.strptime(dateandtime, "%Y-%m-%d %H:%M:%S.%f")
            hour = dateandtime1.hour             #extracting the hours
            
            if hour in hour_counts:
                hour_counts[hour] += 1
            else:
                hour_counts[hour] = 1

hours = sorted(hour_counts.keys())
counts = [hour_counts[hour] for hour in hours]

plt.bar(hours, counts)
plt.xlabel('Hours of the Day')
plt.ylabel('Content Consumption Count')
plt.title('Content Consumption Distribution')
plt.show()
