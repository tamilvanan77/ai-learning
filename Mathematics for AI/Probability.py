#probability

favorable = 3
total = 6

probability = favorable / total

print("Probability:", probability)


#practice

red=5
blue=3
green=2

total=red+blue+green

print(f"Total no of Balls :{total}")
print(f"probability of selecting a red ball{red/total}")
print(f"probability of selecting a blue ball{blue/total}")
print(f"probability of selecting a green ball{green/total}")
print(f"probability of selecting a all ball{total/total}")


#Independent & Dependent Events

#Independent
#Two events are independent when the result of one event does not affect the other event.

#Dependent Events
#Two events are dependent when the result of one event affects the other event.


#Practice

r = 6
b = 4
total = r + b

first_red = r / total
second_red = (r - 1) / (total - 1)
both_red = first_red * second_red

print(f"Probability that the first ball is Red: {first_red:.2f}")
print(f"Probability that the second ball is Red, assuming the first ball was Red: {second_red:.2f}")
print(f"Probability that both balls are Red: {both_red:.2f}")


#Conditional Probability
#Conditional probability means finding the probability of an event when we already know that another event has happened.


even_numbers = [2, 4, 6]

favorable = 1
total = len(even_numbers)

probability = favorable / total

print("P(6 | Even):", probability)


#Practice

stud=20  
stud_py=12
stud_java=8 
stud_both_cls=5 

print(f"probability that a student knows Java given that the student knows Python :{stud_both_cls/stud_java:.2f}")


#Statistics — Variance 📊

#You already learned Standard Deviation. Now let's understand the concept behind it: Variance.

#What is Variance?

#Variance tells us how spread out the values are from the mean.

import numpy as np

marks = [10, 20, 30, 40, 50]

variance = np.var(marks)

print("Variance:", variance)


#practice
marks = [20, 25, 30, 35, 40]
print("Variance:", np.var(marks))



#Population vs Sample 📊

#This is an important statistics concept before we finish the Mathematics for AI section.

#1. Population

#Population means the entire group we are interested in.

#Example:

#A college has 5,000 students.

#If we study the marks of all 5,000 students, those 5,000 students are the population.

#2. Sample

#Sample means a smaller group selected from the population.

#Example:

#From the 5,000 students, we select 100 students for analysis.

import numpy as np

marks = [20, 25, 30, 35, 40]

print("Population Variance:", np.var(marks))
print("Sample Variance:", np.var(marks, ddof=1))



#practice
marks = [20, 25, 30, 35, 40]
print("Population Variance:",np.var(marks))

print ("Sample variance:",np.var(marks,ddof=1))