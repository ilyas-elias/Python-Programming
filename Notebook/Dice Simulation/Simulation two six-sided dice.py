# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 23:47:20 2022

@author: ILYAS
"""

import random
roll = 500

#Dynamic counter 
numbers_count = [0, 0, 0, 0, 
                 0, 0, 0, 0, 
                 0, 0, 0]

#Fixed Data
dice_total = [2, 3, 4, 5, 
              6, 7, 8, 9, 
              10, 11, 12]



for x in range(roll):
    diceTotal = random.randint(1,6) + random.randint(1,6)
    print(numbers_count)
    counter = 0 #declare a variable and alway set to 0 when come a new loop   
    
    for z in dice_total:
        if z == diceTotal:
            numbers_count[counter] = numbers_count[counter] + 1
        counter = counter + 1     
print(numbers_count)
print("Total  \tSimulated Percentage")

count = 2
finCount= 0
for y in range(len(numbers_count)):
     print(y+2, "\t\t", '{0:.2f}'.format(float(numbers_count[y]/5)))
     if max(numbers_count) == numbers_count[y]:
         finCount = count
     count=count+1
     
print("\nTotal :\t",finCount)
print("Highest Simulated Percentage :\t",'{0:.2f}'.format((max(numbers_count)/5)))
print(numbers_count)