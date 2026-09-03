#denominations
a = 1000
b = 500
c = 200
d = 100
e = 50
f = 20
g = 10
h = 5
i = 1

Mon_dep = int(input("Enter your deposit money ---> ")) #should be changeable

#output sentence & its value
print("The deposit money is --->", Mon_dep)

#key block
#rem = remainder
rem_a = Mon_dep % a
rem_b = rem_a % b 
rem_c = rem_b % c 
rem_d = rem_c % d 
rem_e = rem_d % e 
rem_f = rem_e % f 
rem_g = rem_f % g 
rem_h = rem_g % h 
rem_i = rem_h % i


#calculations
print(a, "=", Mon_dep//a)  
print(b, "=", rem_a//b) 
print(c, "=", rem_b//c) 
print(d, "=", rem_c//d) 
print(e, "=", rem_d//e)  
print(f, "=", rem_e//f)  
print(g, "=", rem_f//g)  
print(h, "=", rem_g//h) 
print(i, "=", rem_h//i) 





