def display_global ():
    global variable_1
    variable_1 = variable_1 + 1
    print (id(variable_1))
    print (variable_1)


variable_1 = 2
display_global ()
print (id(variable_1))
print (variable_1)
