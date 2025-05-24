import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_G_cm(epsilon_i, epsilon, wavelength_cm, a_prime_cm, a_cm):
    """
    Compute G(γ'a') using Goubau's formulation (all distances in cm).

    Parameters:
    - epsilon_i: relative permittivity of dielectric (e.g., 2.25)
    - epsilon: relative permittivity of outer medium (e.g., 1.0 for air)
    - wavelength_cm: free-space wavelength in cm
    - a_prime_cm: outer radius of dielectric in cm
    - a_cm: radius of conductor in cm

    Returns:
    - G: value of G(γ'a') [dimensionless]
    """

    ln_ratio = np.log(a_prime_cm / a_cm)
    epsilon_ratio = epsilon_i / (epsilon_i - epsilon)
    lambda_over_a_sq = (wavelength_cm / a_prime_cm) ** 2

    G = ln_ratio / (epsilon_ratio * lambda_over_a_sq)
    return G


# === Example Usage ===
epsilon_i = 4      # dielectric permittivity (e.g., polyethylene)
epsilon = 1.0         # outer medium (air)
wavelength_cm = 50.0  # wavelength = 10 cm (3 GHz)
a_prime_cm = 1      # outer dielectric radius = 1 cm
a_cm = 1-5.6*10**(-2)            # conductor radius = 0.1 cm

G_value = calculate_G_cm(epsilon_i, epsilon, wavelength_cm, a_prime_cm, a_cm)
print(f"G(γ'a') = {G_value:.4e}")

#Substitute this G value into the 
