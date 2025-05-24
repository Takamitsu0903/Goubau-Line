"""
calculate_G_from_geometry.py

This script computes the dimensionless G(γ′a′) function from Goubau’s formulation 
based on physical geometry and material parameters of a Goubau line. 

The formula used is derived from Goubau’s analytical approximation:

    G(γ′a′) = ln(a′/a) / [ (εᵢ / (εᵢ - ε)) * (λ / a′)^2 ]

Where:
- a: inner conductor radius [cm]
- a′: outer radius of the dielectric layer [cm]
- εᵢ: relative permittivity of dielectric
- ε: permittivity of outer medium (usually air = 1)
- λ: free-space wavelength [cm]

Inputs:
- εᵢ: dielectric constant of the coating material (e.g., polyethylene = 2.25–4)
- ε: surrounding medium permittivity (typically 1.0 for air)
- λ: wavelength in cm (e.g., 50 cm = 600 MHz)
- a′: dielectric outer radius in cm
- a: conductor radius in cm

Returns:
- G: computed value of G(γ′a′), dimensionless

Example usage is included for:
- polyethylene dielectric
- air as the outer medium
- λ = 50 cm (600 MHz)
- a′ = 1 cm, a = 0.944 cm

Author: Takamitsu0903
"""

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
