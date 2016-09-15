import numpy as np
from scipy.stats.stats import pearsonr

x = np.arange(-1,1,0.01)
y = x*x


print pearsonr(x,y)
print np.corrcoef(x,y)