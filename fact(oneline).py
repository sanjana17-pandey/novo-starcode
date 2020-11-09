"""
Factorial one-liner
How it works:
    You give a number as input,typecast that as int
    for that number it now calculates by using eval(evaluate function)
    incrementation of x by 1 till the last number is reached.
    and * mark is joined with every x+1 which is now converted to string
Example:
    for 2 in 5: do 2+1=3 do "3" and join to previous (1+1) by *
    after all are joined that is: 1*2*3*4*5
    now we evaluate the factorial and print it
"""


print("\nFactorial:",eval('*'.join(str(x+1) for x in range(max(1, int(input("A number:")))))))
