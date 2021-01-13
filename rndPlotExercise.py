import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

fig, ax = plt.subplots()

a, m = 3., 2.
s = (np.random.pareto(a, 1000) + 1) * m


count, bins, _ = plt.hist(s, 100, density=True)
#count, bins, _ = ax.hist(s, 100, density=True)

fit = a*m**a / bins**(a+1)
plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
count, bins, _ = plt.hist(s, 100, density=True)

st.pyplot(fig)
#plt.show()

