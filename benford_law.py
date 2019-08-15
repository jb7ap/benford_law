import pandas as pd
import matplotlib as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('file:///Users/jason.bang/Documents/all-pos-20190815.csv')

totals = []
first_digit = []
each_digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
digit_counts = []
benford_percents = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
test_percents = []
itr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
error = []

total = df.order_total.astype(float)
total_int = total * 100
for x in total_int:
    totals.append(str(x))

for x in totals:
    first_digit.append(x[0])

for x in each_digit:
    g = first_digit.count(str(x))
    digit_counts.append(g)

for x in digit_counts:
    test_percents.append(x / sum(digit_counts)*100)

for x in itr:
    error.append(abs(test_percents[x] - benford_percents[x])/benford_percents[x])

y_pos = np.arange(len(each_digit))

p1 = plt.bar(y_pos, test_percents, align='center', alpha=0.5)
p2 = plt.bar(y_pos, benford_percents, align='center', alpha=0.5)
plt.xticks(y_pos, each_digit)
plt.ylabel('Count')
plt.title("Benford's Law on all Order Totals")
plt.legend((p1[0], p2[0]), ('Routes', 'Benford'))

plt.show()

