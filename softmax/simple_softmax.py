import math 
layer_output = [4.8,1.21,2.385]

E = math.e

exp_values = []

for output in layer_output:
    exp_values.append(E**output)
    
    
print(exp_values)

norm_base = sum(exp_values)

norm_values = []

for values in exp_values:
    norm_values.append( values / norm_base)
    
print(norm_base)
print(sum(norm_values))