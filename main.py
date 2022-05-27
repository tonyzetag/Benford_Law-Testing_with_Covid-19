from math import log10
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

digits = np.array([1,2,3,4,5,6,7,8,9])

def benford_dist(d):
	return log10(1 + (1/d))

y = [benford_dist(d) for d in range(1,10)]

# Import data, (cases)
ds = pd.read_csv('covid-19.csv')

# Drop zero data
ds = ds[ds['cases'] > 0]

# Transform
ds['first_digit_cases'] = [int(str(n)[0]) for n in ds['cases']]

# Probability
p = [np.sum(ds['first_digit_cases'] == d) for d in digits]
p = p/np.sum(p)

plt.bar(digits, height=p, color = 'blue', label='cases', alpha=0.5)

# Drop zero data
ds = ds[ds['deaths'] > 0]

# Transform
ds['first_digit_deaths'] = [int(str(n)[0]) for n in ds['deaths']]

# Probability
p = [np.sum(ds['first_digit_deaths'] == d) for d in digits]
p = p/np.sum(p)

plt.bar(digits, height=p, color = 'green', label='deaths', alpha=0.5)

plt.plot(digits, y, c='red')
plt.legend()
plt.show()