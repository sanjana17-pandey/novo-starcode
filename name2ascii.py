"""
#######################################
#    Name to ASCII                    #
#######################################
    conversion of name into its
    corresponding ASCII codes
"""
array=list(input("Name:"))        #name input

print("\nYour name in ASCII:\n")  #display
for i in array:                   #for each in name
    print(i,"=",ord(i))           #compute
    
