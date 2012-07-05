'''
Created on Jul 5, 2012

@author: NEXT Speed
'''
highest_score=0
result_f = open("result.txt")

for line in result_f:
    (name,scores) = line.split()
    if float(scores) >  highest_score:
        highest_score = float(scores)
        
print("highest scores:")
print(highest_score)
