import csv


#with open("C:\\Users\\Saagar\\PycharmProjects\\AstroProject\\myData.csv", "r") as f:
#    file_contents = f.read()
#    print(file_contents)

iss_mass = 420000
with open("testFile.txt", "w") as w:
    w.write("hello")

with open("C:\\Users\\Saagar\\PycharmProjects\\AstroProject\\myData.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("C:\\Users\\Saagar\\PycharmProjects\\AstroProject\\newFile.csv", "w") as new_file:
        fieldnames=["Force(pitch)","Force(roll)","Force(yaw)","Time(s)"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()

    for row1 in csv_reader:
        try:
            row2 = next(csv_reader, None)
            if (row2 is None):
                break  # end of file
            force_yaw = float(row1["accel_yaw"]) - float(row2["accel_yaw"])
            force_pitch = float(row1["accel_pitch"]) - float(row2["accel_pitch"])
            force_roll = float(row1["accel_roll"]) - float(row2["accel_roll"])
            csv_writer.writerow([force_pitch, force_roll, force_yaw, "9"])
        except csv.Error:
            pass
#use try except block like chatgpt said
        #print(f"first row: {row1}; second row: {row2}")



        #print(line["gyro_pitch"])
        #force_pitch = line["accel_pitch"]
        #force_roll = line["accel_roll"]
        #force_yaw = line["accel_yaw"]
        #csv_writer.writerow([])