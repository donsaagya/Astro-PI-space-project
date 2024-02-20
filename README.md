# Astro-PI-Mission-SpaceLab-Project

When the ISS is in orbit, it needs to maintain its orientation in order to keep facing the earth.
The ISS does this by either using the Russian Truss Segment and the Control Moment Gyroscopes.


The aim of this project was to calculate the torques/moments for the ISS, and the energy consumed.
data_collector.py was executed on the ISS.
myData was the data that was collected from execution.
myData contains data regarding the acceleration and position values (with units as degrees) in the 3 rotational axes(pitch, roll, yaw) with respect to time.


From the large amount of data collected, we can observe and study the rapid changes in orientation of the ISS.
These rapid changes are highly likely to have been performed with the help of the Fueled Truss Segment.
From these torques, we can derive how much energy was consumed in changing the orientation.
