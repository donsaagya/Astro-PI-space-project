from sense_hat import SenseHat
import datetime
import csv
from time import sleep, time
from pathlib import Path

# function that obtains orientation in roll, pitch and yaw
def rasp_orientation():

    rotation = sense.get_orientation()

    pitch = rotation["pitch"]
    roll = rotation["roll"]
    yaw = rotation["yaw"]

    return roll, pitch, yaw,


# function calculates the rate of change of orientation or angular freq/speed in the roll, pitch and yaw axes
def calc_speed():
    # obtain starting position and time
    initial_roll, initial_pitch, initial_yaw = rasp_orientation()
    start_time = datetime.datetime.now()

    #time interval
    sleep(0.1)

    # obtain end position and time
    final_roll, final_pitch, final_yaw = rasp_orientation()
    finish_time = datetime.datetime.now()

    #list with distance travelled or change in orientation.
    change_in_orientation = [final_roll - initial_roll, final_pitch - initial_pitch, final_yaw - initial_yaw]
    time_passed = (finish_time - start_time).total_seconds()

    #list will contain speeds in all rotating axes.
    speed = []

    for change in change_in_orientation:
        # Energy consumed regardless of direction hence change monitored as positive
        change = abs(change)
        # calculating speed and adding calculated value to the speed list
        speed.append(change/time_passed)

    # Unpacking to give each list item their description or variable/container
    roll_speed, pitch_speed, yaw_speed = speed

    return roll_speed, pitch_speed, yaw_speed


# function that calculates accelertation
def calc_acceleration():

    #remains false if value obtained is 0. hence won't display anything on SENSE HAT.
    acceleration_detected = False

    # obtain starting speed and time
    initial_roll, initial_pitch, initial_yaw = calc_speed()
    start_time = datetime.datetime.now()

    sleep(0.1)

    # obtain end speed and time
    final_roll, final_pitch, final_yaw = calc_speed()
    finish_time = datetime.datetime.now()

    #list with changes in speed travelled.
    change_in_speed = [final_roll - initial_roll, final_pitch - initial_pitch, final_yaw - initial_yaw]
    time_passed = (finish_time - start_time).total_seconds()
    acceleration = []

    for change in change_in_speed:

        # Energy consumed regardless of direction hence change monitored as positive
        change = abs(change)
        if change != 0:
            #set condition to display to True
            acceleration_detected = True

        # calculating acceleration and adding calculated value to the acceleration list
        acceleration.append(change/time_passed)

    # Unpacking to give each list item their description or variable/container
    roll_acceleration, pitch_acceleration, yaw_acceleration = acceleration

    return roll_acceleration, pitch_acceleration, yaw_acceleration, time_passed, acceleration_detected


#rotates screen depending if rasp SENSE hat rotated
def rotate_screen():
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)

  # Update the rotation of the display depending on which way up the Sense HAT is
	if x  == -1:
	  sense.set_rotation(90)
	elif y == -1:
	  sense.set_rotation(180)
	elif y == 1:
	  sense.set_rotation(0)
	elif x == 1:
	  sense.set_rotation(270)


#--------------------------------------------CODE STARTS HERE----------------------------------------------------------
start_time = datetime.datetime.now()
time_now = datetime.datetime.now()

#stores path of this code which can be used to store csv file in same location
dir_path = Path(__file__).parent.resolve()

#creating object to use the SENSE HAT
sense = SenseHat()

#clear screen
sense.clear()

#create csv file and csv writer
data_file = open(f"{dir_path}/data01.csv", "w")
writer = csv.writer(data_file)

#titles
writer.writerow(["accel_roll","accel_pitch", "accel_yaw", "time(s)", "gyro_roll", "gyro_pitch", "gyro_yaw", "time_now"])

#program stops 10 seconds before end of 3 hours time.
while (time_now < start_time + datetime.timedelta(minutes = 179.82)):
    try:
        sense.clear()

        #display depending on which way rasp pi is facing.
        rotate_screen()

        #acceleration in the form (ms^-2) will be calculated back on earth
        #these acceleration values will have units (θs^-2)
        accel_roll, accel_pitch, accel_yaw, time_taken, display = calc_acceleration()

        # will use these to calculate distance travelled from equation (arc length = radius * θ)
        gyro_roll, gyro_pitch, gyro_yaw = rasp_orientation()

        if display == True:
            sense.show_letter("!", text_colour = (70, 70, 70))

        # what time is it after calculations without microseconds
        time_now = datetime.datetime.now().time().replace(microsecond = 0)

        writer.writerow([accel_roll, accel_pitch, accel_yaw, time_taken, gyro_roll, gyro_pitch, gyro_yaw, time_now])

        sleep(0.1)

        # update time at the end of loop
        time_now = datetime.datetime.now()

    except:
        writer.writerow([f"An error occured! Values not taken at time:{time_now.time()}"])
        time_now = datetime.datetime.now()

#write start time without microseconds
writer.writerow([f"start_time: {start_time.time().replace(microsecond = 0)}"])

time_now = datetime.datetime.now()

#write end time without microseconds
writer.writerow([f"end_time: {time_now.time().replace(microsecond = 0)}"])
data_file.close()
sense.clear()