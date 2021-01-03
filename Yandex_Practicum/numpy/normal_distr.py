from scipy import stats as st

mu = 100500
sigma = 3500

bonus_threshold = 111000
penalty_threshold = 92000

p_bonus = 1 - st.norm(mu, sigma).cdf(bonus_threshold)
p_penalty = st.norm(mu, sigma).cdf(penalty_threshold)

print('Bonus probability:', p_bonus)
print('Penalty probability:', p_penalty)