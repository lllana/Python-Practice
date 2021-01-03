from scipy import stats as st
import numpy as np
import pandas as pd

revenue = pd.Series([727, 678, 685, 669, 661, 705, 701, 717, 
                     655,643, 660, 709, 701, 681, 716, 655, 
                     716, 695, 684, 687, 669,647, 721, 681, 
                     674, 641, 704, 717, 656, 725, 684, 665])

interested_value = 800

alpha = .05

results = st.ttest_1samp(
        revenue, 
        interested_value)

print('p-value:', results.pvalue / 2)

if (results.pvalue / 2 < alpha) and (revenue.mean() < interested_value):
    # and check to see if the sample mean is on the correct side of interested_value):
    print("We reject the null hypothesis: revenue was significantly lower than 800 dollars")
else:
    print("We can't reject the null hypothesis: revenue wasn't significantly lower")