from scipy import stats as st

mu = 420
sigma = 65

prob = 0.9

n_shipment = st.norm(mu, sigma).ppf(1 - prob)

print('Need to order items:', int(n_shipment))