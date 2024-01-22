import numpy as np
from matplotlib import pyplot as plt
import math
import sys

print(sys.argv[1])
if sys.argv[1] not in ["parabola", "weight", "force"]:
  print("'parbola' or 'weight' or 'force' ?")
  exit(1)
graph_type = sys.argv[1] 

# Cooefficients of friction for steel - The Physics Factbook
static_friction_steel_max = 0.6
static_friction_steel_min = 0.15
weight_rollercoaster_kg = 40000
x_frictional_force=[]
y_frictional_force= []
x_weight_in_dir_incline=[]
y_weight_in_dir_incline=[]


def graph(x, x_description, y, y_description, title, nr):
    plt.plot(x_frictional_force, y_frictional_force)
    plt.xlabel(x_description)
    plt.ylabel(y_description)
    plt.title(title)
    plt.show()

# Define parabola
def f(x): 
    return x**2

# Define parabola derivative
def slope(x): 
    return 2*x

def get_angle(x1,y1,x2,y2):
    return math.degrees(math.radians(90) - math.atan2(y2-y1, x2-x1))


x1_hold = 0
y1_hold = 0
def find_all_angles(x1_hold, y1_hold):
    all_angles = []
    for val in range(-5,2):
        xrange = np.linspace(val-1, val+1, 10)
        x1 = val
        if x1_hold == 0:
            x1_hold = x1
        y1 = f(x1)
        if y1_hold == 0:
            y1_hold = x1
        angle = get_angle(x1_hold, y1_hold, x1, y1)
        all_angles.append(angle)
    return all_angles      
all_angles = find_all_angles(x1_hold, y1_hold)
angle_max = max(all_angles)
angle_min = min(all_angles)




def calc(static_friction, weight, angle):
    a = math.radians(angle)

    # normal force
    force = weight * math.cos(a)

    # frictional force
    frictional_force = force * static_friction

    # weight in dir incline
    weight_incline = weight * math.cos(math.radians(90 - angle))

    #print("Frictional force", frictional_force)
    #print("Weight in direction of incline", weight_incline)
    return (frictional_force, weight_incline)

def calc_static_friction_increment(increment):
    step = (static_friction_steel_max - static_friction_steel_min)/(angle_max - angle_min)
    #print("static_friction_steel_max - static_friction_steel_min", static_friction_steel_max - static_friction_steel_min)
    #print("----", step  * increment)
    return step * increment

# Define x data range for parabola
x = np.linspace(-5,5,100)

# Choose point to plot tangent line
x1 = -3
y1 = f(x1)

# Define tangent line
# y = m*(x - x1) + y1
def line(x, x1, y1):
    return slope(x1)*(x - x1) + y1

# Define x data range for tangent line
xrange = np.linspace(x1-1, x1+1, 10)

# Plot the figure
plt.figure()
plt.plot(x, f(x))
plt.scatter(x1, y1, color='C1', s=50)

counter = -5


for val in range(-5,2):
    xrange = np.linspace(val-1, val+1, 10)
    x1 = val
    if x1_hold == 0:
        x1_hold = x1
    y1 = f(x1)
    if y1_hold == 0:
        y1_hold = x1
    angle = get_angle(x1_hold, y1_hold, x1, y1)
    print(angle)

    static_friction_increment = calc_static_friction_increment(angle)
    #print(">>>>> ", static_friction_increment )
    #print(">>>>> ststic friction value ", static_friction_steel_min + static_friction_increment )
    res = calc(static_friction_steel_min + static_friction_increment, weight_rollercoaster_kg, angle)
    x_frictional_force.append(angle)
    y_frictional_force.append(res[0])
    x_weight_in_dir_incline.append(angle)
    y_weight_in_dir_incline.append(res[1])

    print("slope >> ", slope(x1) )
    plt.plot(xrange, line(xrange, x1, y1), 'C1--', linewidth = 2)
    print(x_weight_in_dir_incline)
    print(y_weight_in_dir_incline)
    counter+=1
if graph_type == "parabola":    
    plt.show()
    plt.close()
elif graph_type == "weight":
    plt.clf()
    plt.cla()
    graph(x_weight_in_dir_incline, "Angle (°)", y_weight_in_dir_incline, "Weight in direction of incline (Kg)", 'How weight in direction of incline changes with ° of the roller coaster from 0° to 90°', 2)
else:
    plt.clf()
    plt.cla()
    graph(x_frictional_force, "Angle (°)", y_frictional_force, "Force (N)", 'How force changes with ° of the roller coaster from 0° to 90°', 2)