from scipy import stats as st
import numpy as np

# time spent on the website by users with a username and password
time_on_site_logpass = [368, 113, 328, 447, 1, 156, 335, 233, 
                       308, 181, 271, 239, 411, 293, 303, 
                       206, 196, 203, 311, 205, 297, 529, 
                       373, 217, 416, 206, 1, 128, 16, 214]

# time spent on the website by users signing in through social media
time_on_site_social  = [451, 182, 469, 546, 396, 630, 206, 
                        130, 45, 569, 434, 321, 374, 149, 
                        721, 350, 347, 446, 406, 365, 203, 
                        405, 631, 545, 584, 248, 171, 309, 
                        338, 505]


# your code goes below

alpha = .05

results = st.ttest_ind(
            time_on_site_logpass,
            time_on_site_social)

print('p-value:', results.pvalue)

if (results.pvalue < alpha):
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")