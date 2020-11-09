"""
#############################################
#  For a given decimal number as input,     #
#  this code will convert the decimal       #
#  number into equivalent binary number.    #
#############################################
"""

number=int(input("Decimal Number:"))  #input of decimal number
temp=number                           #store it
binary=""                             #string to store the binary number
while number>0:
    rem=number%2
    binary+=str(rem)
    number=number//2

#display of processed number
print("The binary equivalent of "+str(temp)+" is "+binary[::-1]+" .")
