#importing the libraries

import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats

#creating distributions
N = 10001
nbins = 30

d1 = np.random.randn(N) - 1
d2 = 3 * np.random.randn(N)
d3 = np.random.randn(N) + 1


y1, x1 = np.histogram(d1,nbins)
x1 = (x1[1:] + x1[:-1])/2

# y2, x2 = np.histogram(d2,nbins)
# x2 = (x2[1:] + x2[:-1])/2

y3, x3 = np.histogram(d3,nbins)
x3 = (x3[1:] + x3[:-1])/2


#plotting the Distributions

plt.plot(x1,y1,'b')
plt.plot(x2,y2,'r')
plt.plot(x3,y3,'k')

plt.show()


#calculating the mean

mean_d1 = d1.mean()
mean_d2 = d2.mean()
mean_d3 = d3.mean()

plt.plot(x1, y1, 'b', x2, y2, 'r', x3,  y3, 'k')
plt.plot([mean_d1,mean_d1],[0,max(y1)],'b--')
plt.plot([mean_d2,mean_d2],[0,max(y2)],'r-')
plt.plot([mean_d3,mean_d3],[0,max(y3)],'k--')

plt.show()

#Mean Failing Case
d4 = np.hstack((np.random.randn(N) - 2 , np.random.randn(N)+2))

y4, x4 = np.histogram(d4, nbins)
x4 = (x4[1:] + x4[:1])/2

plt.plot(x4,y4)
plt.plot([x4.mean(), x4.mean()], [0, max(y4)])
plt.show()

#Making the Log Normal Distribution

N = 10001
stretch = 0.7 
shift = 0
nbins = 50 

data = stretch * np.random.randn(N) + shift
data = np.exp(data)

y, x = np.histogram(data, nbins)
x = (x[:1] + x[1:])/2

#showing the Median With the Graph

plt.plot(x,y,'k')
plt.plot([np.median(data), np.median(data)],[0, max(y)],'k--')
plt.show()


numbers = np.round(np.random.randn(10))

for i in numbers