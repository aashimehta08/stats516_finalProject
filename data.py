import csv
import random
import matplotlib.pyplot as plt
from scipy.stats import shapiro 


with open('SOCR-HeightWeight.csv', 'r') as height_file :
    csv_reader = csv.reader(height_file)
    next(csv_reader)

    heights = []

    for line in csv_reader :
        heights.append(float(line[1]))

    sample = random.sample(heights, 1000)

    print(shapiro(sample))
    plt.hist(sample, bins = 12, edgecolor = 'black')
    plt.xlabel("Height of a 18 year old/inches")
    plt.ylabel("Frequency")
    plt.title("1000 random samples")
    plt.show()

