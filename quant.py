"""Option pricing for the Options Lab (numpy only, no scipy)."""

import math

import numpy as np

_erf = np.vectorize(math.erf, otypes=[float])
SQRT2 = math.sqrt(2.0)
INV_SQRT_2PI = 1.0 / math.sqrt(2.0 * math.pi)


def norm_cdf(x):
    return 0.5 * (1.0 + _erf(np.asarray(x, dtype=float) / SQRT2))


def norm_pdf(x):
    x = np.asarray(x, dtype=float)
    return INV_SQRT_2PI * np.exp(-0.5 * x * x)


# ---------------------------------------------------------------- Black-Scholes
def black_scholes(S, K, T, r, sigma, kind="call"):
    """Price and Greeks. Vega/rho per 1% move, theta per calendar day."""
    S = np.asarray(S, dtype=float)
    T = max(T, 1e-8)
    sigma = max(sigma, 1e-8)
    sqrtT = math.sqrt(T)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    disc = math.exp(-r * T)
    pdf_d1 = norm_pdf(d1)

    if kind == "call":
        price = S * norm_cdf(d1) - K * disc * norm_cdf(d2)
        delta = norm_cdf(d1)
        theta = -S * pdf_d1 * sigma / (2 * sqrtT) - r * K * disc * norm_cdf(d2)
        rho = K * T * disc * norm_cdf(d2)
    else:
        price = K * disc * norm_cdf(-d2) - S * norm_cdf(-d1)
        delta = norm_cdf(d1) - 1.0
        theta = -S * pdf_d1 * sigma / (2 * sqrtT) + r * K * disc * norm_cdf(-d2)
        rho = -K * T * disc * norm_cdf(-d2)

    return {
        "price": price,
        "delta": delta,
        "gamma": pdf_d1 / (S * sigma * sqrtT),
        "vega": S * pdf_d1 * sqrtT / 100.0,
        "theta": theta / 365.0,
        "rho": rho / 100.0,
    }


def binomial_crr(S, K, T, r, sigma, kind="call", steps=300, american=False):
    """Cox-Ross-Rubinstein binomial tree, European or American exercise."""
    dt = T / steps
    u = math.exp(sigma * math.sqrt(dt))
    d = 1.0 / u
    p = (math.exp(r * dt) - d) / (u - d)
    disc = math.exp(-r * dt)

    j = np.arange(steps + 1)
    prices = S * u ** (steps - j) * d**j
    payoff = np.maximum(prices - K, 0) if kind == "call" else np.maximum(K - prices, 0)
    values = payoff

    for i in range(steps - 1, -1, -1):
        values = disc * (p * values[:-1] + (1 - p) * values[1:])
        if american:
            prices = prices[:-1] * d  # = S * u**(i-j) * d**j
            exercise = prices - K if kind == "call" else K - prices
            values = np.maximum(values, exercise)
    return float(values[0])
