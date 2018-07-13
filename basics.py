import csv

csv_data = []

with open('ks-projects-201801.csv', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        csv_data.append(row)

print("-" * 15 + "Python List" + "-" * 15)
print("Type: {}\n".format(type(csv_data)))
print("Header: {}\n".format(csv_data[0]))
print("1st record: {}\n".format(csv_data[1]))
print("1st record category: {}\n".format(csv_data[1][2]))

import numpy


np_data = numpy.array(csv_data)

print("-" * 15 + "Numpy Array" + "-" * 15)
print("Type: {}\n".format(type(np_data)))
print("Shape: {}\n".format(np_data.shape))
print("Header: {}\n".format(np_data[0]))
print("1st record: {}\n".format(np_data[1]))
print("1st record category: {}\n".format(np_data[1][2]))

np_goals = np_data[1:,6]
np_pleged = np_data[1:,8]
np_status = np_data[1:,9]
import matplotlib.pyplot

matplotlib.pyplot.hist(np_status[:])
matplotlib.pyplot.show()

import pandas

pandas_data = pandas.read_csv("ks-projects-201801.csv", index_col=0)
print(pandas_data[:4])

print(pandas_data.index)

print(pandas_data.loc[:, 'main_category'])


'''
RESEARCH Q's

Easy
1. What percent of kickstarters reached their goal?
2. How many different categories are there?
3. What percent of all kickstarters in each category
4. Total money pledged in all kickstarters
5. Total money collected ain all kickstarters

Medium
1. Are specific categories of kickstarters more successful than others?
    a. Define successful -- kickstarters definition, % goal pledged, etc.

2. Is there a correlation between category and likelihood to succeed?f

3. most popular kickstarters by country -- are they looking for funding by specific categories

4. GoFundme -- ppl trying to raise money for healthcare

5. Social connections -- kickstarters in America, are there more trends over specific categories like health care solutions
    a. socially oriented category like healthcare and tie that to government spending for social programs

6. sweet spot of asking for money
    a. by category

7. Success vs time

8. Category popularity over time




'''

