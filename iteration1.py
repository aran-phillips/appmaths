import math
import matplotlib.pyplot as plt 


angle_min = 0
angle_max = 90
#source wikipedia shuttle loop
weight_rollercoaster_kg = 40000 

def calc(weight, angle):

    # weight in dir incline
    weight_incline = weight * math.cos(math.radians(90 - angle))

    return weight_incline






def graph(x, x_description, y, y_description, title, nr):
    plt.clf()
    plt.cla()
    plt.plot(x, y)
    plt.xlabel(x_description)
    plt.ylabel(y_description)
    plt.title(title)
    plt.show()
    plt.close()


x_weight_in_dir_incline=[]
y_weight_in_dir_incline=[]


# angle from 0 to 90
for angle_increment in range(0, 91):
    #print(angle_increment)
    res = calc(weight_rollercoaster_kg, angle_increment)
    x_weight_in_dir_incline.append(angle_increment)
    y_weight_in_dir_incline.append(res)
		

print(x_weight_in_dir_incline)
print(y_weight_in_dir_incline)
graph(x_weight_in_dir_incline, "Angle (°)", y_weight_in_dir_incline, "Weight in Direction of incline (Kg)", 'How Weight changes with angle of the Roller Coaster from 0° to 90°', 2)



