import matplotlib.pyplot as plt
import numpy as np

data = np.random.default_rng(19680801)

n_points = 10000
n_bins = 20

#Generate two normal distributions
d1 = data.standard_normal(n_points)
d2 = 0.5 * data.standard_normal(n_points)+5

fig, ax = plt.subplots(1,2)
ax[0].hist(d1, bins=n_bins)
ax[1].hist(d2, bins=n_bins)
plt.show()
