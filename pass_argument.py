def display_global (variable_func):
    print ("variable_func")
    print (id(variable_func))
    print (variable_func)        
    variable_1 = variable_func + 0
    variable_func += variable_func
    print ("variable_func")
    print (id(variable_func))
    print (variable_func)
    print ("variable_1")
    print (id(variable_1))
    print (variable_1)
    return variable_func

variable_1 = 2
print ("variable_1")
print (id(variable_1))
print (variable_1)
display_global (variable_1)
print ("variable_1")
print (id(variable_1))
print (variable_1)
return_value = display_global (variable_1)
print ("return_value")
print (id(return_value))
print (return_value)