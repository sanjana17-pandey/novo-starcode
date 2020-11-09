"""
###############################################
# Distnace between two points in 2-dimensions #
###############################################
"""

print("\nThis porgram finds the distance between two points in 2-D space")
print("Enter the values:-\n")
x1=float(input("x1="))                 #user input(line8-11)
x2=float(input("x2="))
y1=float(input("y1="))
y2=float(input("y2="))

import math                            #importing math module
sol1=pow((x2-x1),2)+pow((y2-y1),2)     #computing
sol2=round(math.sqrt(sol1),2)

print("\nDistance between","(",x1,",",y1,")","and (",x2,",",y2,"):",sol2,"\n")        
