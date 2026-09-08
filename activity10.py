x = 10
y = 15
z = 20

print(x < y or y > z) #true
print(x > z and y < z) #false
print(x > y or y > z and z != x) #false
print(x > y and y > z or z != x) #true
print(not(x < y or y > z and z != x)) #false


#order of precedence
#not, and, or