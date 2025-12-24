import pandas as pd
import matplotlib.pyplot as plt

data = {
    'ride_type': ['Short Ride', 'Long Ride', 'Short Ride', 'Long Ride', 'Short Ride', 'Long Ride'],
    'trip_distance': [1.2, 10.5, 2.3, 15.1, 1.0, 20.0]
}
df = pd.DataFrame(data)

summary_stats = df.groupby('ride_type')['trip_distance'].describe()
print("Summary Statistics:\n", summary_stats)

plt.figure(figsize=(10, 6))


df[df['ride_type'] == 'Short Ride']['trip_distance'].hist(
    bins=10, alpha=0.7, label='Short Ride', color='skyblue', edgecolor='black'
)

df[df['ride_type'] == 'Long Ride']['trip_distance'].hist(
    bins=10, alpha=0.7, label='Long Ride', color='orange', edgecolor='black'
)

plt.xlabel('Trip Distance (miles)')
plt.ylabel('Number of Trips')
plt.title('Histogram of Ride-Sharing Trip Distances: Short vs Long Rides')
plt.legend()
plt.show()
