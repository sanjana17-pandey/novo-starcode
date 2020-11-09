"""
############################################################
# Computes the distance between two points in 3-dimensions #
############################################################
"""

print("\nThis porgram finds the distance between two points in 3-D space")
print("Enter the values:-\n")
x1=float(input("x1="))              #user input(lines9-14)
x2=float(input("x2="))
y1=float(input("y1="))
y2=float(input("y2="))
z1=float(input("z1="))
z2=float(input("z2="))


import numpy                        #importing numpy module
sol1=pow((x2-x1),2)+pow((y2-y1),2)+pow((z2-z1),2)
sol2=round(numpy.sqrt(sol1),2)      #rounding off the computed value

print("\nDistance between","(",x1,",",y1,",",z1,")","and (",x2,",",y2,",",z2,")",sol2,"\n")
