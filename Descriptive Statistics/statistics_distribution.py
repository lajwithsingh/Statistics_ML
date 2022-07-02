#importing libraries

import numpy as np
import matplotlib.pyplot as plt 
from scipy import stats


#Gaussian Distribution

N = 1001
x = np.linspace(-5, 5, N) 

gausdist = stats.norm.pdf(x)

fig, ax =plt.subplots(1,2, figsize = (10,20))

ax[1].plot(x, gausdist)
ax[1].set_title("Gaussian Distribution Without PDF")

ax[0].plot(x,gausdist*0.08)
ax[0].set_title("Gaussian Distribution With PDF")

fig.savefig("gausdist.png")

plt.show()


#Random Gaussian Distribution

stretch = 5
shift = 15
N = 1000

data = np.random.randn(N) * stretch + shift

plt.hist(data, bins = 50, rwidth=0.5 , color="#acb540")
plt.show()


#Unform Distribution

stretch = 2
shift = .5
N = 10000

data = stretch*np.random.rand(N) + shift-stretch/2

fig, ax = plt.subplots(2,1, figsize=(5,6))

ax[0].plot(data, '.', markersize = 1)
ax[0].set_title('Uniform Data Values')

ax[1].hist(data,25)
ax[1].set_title('Uniform Data Histogram')

plt.show()

#Log Normal Distribution

N = 1001 
x = np.linspace(0, 10, N)

logNormDist = stats.lognorm.pdf(x, 1)

plt.plot(x, logNormDist)
plt.title("Log Normal Distribution")
plt.show()

#Empirical Log Normal Distribution

shift = 5 
stretch = .5
n = 10000

data = np.random.randn(n) * stretch + shift
data = np.exp(data)

fig, ax = plt.subplots(1, 2, figsize = (10,20))

ax[0].plot(data, '.', markersize = 1)
ax[0].set_title('Log Normal Distribution')

ax[1].hist(data, bins = 25)
ax[1].set_title('Log Normal Distribution')

plt.show()

#Binomal Distribution

n = 100 
p = 0.5 

x = range(n+2)
data = stats.binom.pmf(x ,n ,p)

plt.bar(x, data)
plt.title(f"Binomial Distribution (n={n},p={p})")
plt.show()

#t

x = np.linspace(-4, 4, 1001)
df = 200
t = stats.t.pdf(x, df)

plt.plot(x, t)
plt.xlabel("T Values")
plt.ylabel("P(t | H$_0$)")
plt.title('T Distribution')
plt.show()

#f

num_df = 5
den_df = 100

x = np.linspace(0, 10, 10001)

fdist = stats.f.pdf(x,num_df, den_df)

plt.plot(x, fdist)
plt.title(f'F({num_df}, {den_df}) Distribution ')
plt.xlabel('F Value') 

plt.show()