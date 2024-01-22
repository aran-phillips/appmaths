import math
import matplotlib.pyplot as plt 

# Cooefficients of friction for steel - The Physics Factbook
static_friction_steel_max = 0.6
static_friction_steel_min = 0.15

angle_min = 0
angle_max = 90
#source wikipedia shuttle loop
weight_rollercoaster_kg = 40000 

def calc(static_friction, weight, angle):
    a = math.radians(angle)

    # normal force
    force = weight * math.cos(a) 

    # frictional force
    frictional_force = force * static_friction

    #print("Frictional force", frictional_force)
    #print("Weight in direction of incline", weight_incline)
    return frictional_force

def calc_static_friction_increment(increment):
    step = (static_friction_steel_max - static_friction_steel_min)/(angle_max - angle_min)
    #print("static_friction_steel_max - static_friction_steel_min", static_friction_steel_max - static_friction_steel_min)
    #print("----", step  * increment)
    return step	* increment





def graph(x, x_description, y, y_description, title, nr):
    plt.clf()
    plt.cla()
    plt.plot(x, y)
    plt.xlabel(x_description)
    plt.ylabel(y_description)
    plt.title(title)
    plt.show()
    plt.close()

x_frictional_force=[]
y_frictional_force= []


# static friction between 0.6 and 0.15
# angle from 0 to 90
for angle_increment in range(0, 91):
    #print(angle_increment)
    static_friction_increment = calc_static_friction_increment(angle_increment)
    #print(">>>>> ", static_friction_increment )
    #print(">>>>> ststic friction value ", static_friction_steel_min + static_friction_increment )
    res = calc(static_friction_steel_min + static_friction_increment, weight_rollercoaster_kg, angle_increment)
    x_frictional_force.append(angle_increment)
    y_frictional_force.append(res)
    
		
print(x_frictional_force)
print(y_frictional_force)
graph(x_frictional_force, "Roller Coaster Angle (°)", y_frictional_force, "Frictional Force (N)", 'How Frictional Force changes with angle of the Roller Coaster from 0° to 90°', 1)



