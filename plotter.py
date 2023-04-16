import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('C:\\Users\\Saagar\\PycharmProjects\\AstroProject\\myData.csv')

# Extract the pitch and roll data as separate Series
pitch = data['pitch']
roll = data['roll']
time = data['time']

# Plot pitch against time
plt.plot(time, pitch)
plt.xlabel('Time (s)')
plt.ylabel('Pitch (degrees)')
plt.title('Pitch vs Time')
plt.show()

# Plot roll against time
plt.plot(time, roll)
plt.xlabel('Time (s)')
plt.ylabel('Roll (degrees)')
plt.title('Roll vs Time')
plt.show()
