import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('/Users/friend/Desktop/housing.csv')
num_df = data.select_dtypes(include = [np.number])
print(num_df[:].hist(bins = 15, figsize = (15,12)))
plt.show()
