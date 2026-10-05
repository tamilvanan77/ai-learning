#Normal Distribution 🔔

#A Normal Distribution is a common way to describe data where most values are around the mean, and fewer values occur as we move away from the mean.


import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(70, 10, 1000)

plt.hist(data, bins=30)
plt.title("Normal Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()


#practice

mean = 50
std = 5
size = 1000

data=np.random.normal(mean,std,size)

plt.hist(data,bins=100)
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

#z-test

mean = 50
std = 10
x = 70

z = (x - mean) / std

print("Z-Score:", z)

#practice

marks = [40, 50, 60, 70, 80]
mean = 60
std = 10

for mark in marks:
    print("Z Test",(mark-mean)/std)


import numpy as np

population = np.arange(1, 101)

sample = np.random.choice(population, size=10, replace=False)

print("Sample:", sample)
print("Sample Mean:", np.mean(sample))


#practice

import numpy as np
import matplotlib.pyplot as plt

population = np.arange(1, 101)

sample_means = []

for i in range(100):
    sample = np.random.choice(population, size=10, replace=False)
    mean = np.mean(sample)
    sample_means.append(mean)

print("Number of sample means:", len(sample_means))
print("Sample means:", sample_means)

plt.hist(sample_means, bins=10)

plt.title("Distribution of Sample Means")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.show()
