library(extRemes)

# Define the quantile function for the GEV distribution
gev_quantile = function(xi, mu, sigma, p) { qgev(p, loc = mu, scale = sigma, shape = xi) }

# Example usage:
p <- seq(0.01, 0.99, 0.01)  # Probabilities for 
xi <- 0.1  # Shape parameter
mu <- 0  # Location parameter
sigma <- 1  # Scale parameter



quantiles = gev_quantile(xi, mu, sigma, p)

# Plot histogram and quantile-quantile plot
hist(quantiles)
qqplot(quantiles, qgev(p, loc = mu, scale = sigma, shape = xi))




