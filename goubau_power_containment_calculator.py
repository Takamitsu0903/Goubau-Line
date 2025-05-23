import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hankel1
from scipy.optimize import root_scalar

# Exact F function as in Goubau's Eq. 36a
def F(gamma_rho):
    j_gamma_rho = 1j * gamma_rho
    H0 = hankel1(0, j_gamma_rho)
    H1 = hankel1(1, j_gamma_rho)
    term1 = (-2 / gamma_rho) * 1j * H0 * H1
    term2 = -(H0**2 + H1**2)
    return (gamma_rho**2) * (term1 + term2)

# Equation to solve for a given power level p
def compute_rho_ap_for_gamma_ap(gamma_ap, p):
    def equation(rho_ap):
        gamma_rhop = gamma_ap * rho_ap
        return 1 - (F(gamma_rhop) / F(gamma_ap)) - p
    try:
        sol = root_scalar(equation, bracket=[1, 1e4], method='brentq')
        return sol.root
    except ValueError:
        return np.nan

# Parameters
a_prime_cm = 0.105           # Overall outer radius a' in cm
p_target = 0.99            # 90% power containment
gamma_ap_values = np.logspace(-4, -1, 150)

# Compute rho/a' for all gamma'a' values
rho_ap_values = [compute_rho_ap_for_gamma_ap(g, p_target) for g in gamma_ap_values]

# Specific markers
gamma2 = 5.6*10**(-3)     # cm^-1
gamma2_ap = gamma2 * a_prime_cm

rho2_ap = compute_rho_ap_for_gamma_ap(gamma2_ap, p_target)

# Convert normalized rho to cm
rho2_cm = rho2_ap * a_prime_cm

# Plotting
plt.figure(figsize=(8, 6))
plt.loglog(gamma_ap_values, rho_ap_values, label=r"$\rho_{90\%}/a'$ Curve", linewidth=2)
plt.scatter([gamma2_ap], [rho2_ap], color='blue', s=80, label=fr"$\gamma'={gamma2}$ cm$^{{-1}}$, $\rho={rho2_cm:.2f}$ cm") #Plot the specific point

plt.grid(True, which='both', linestyle=':', linewidth=0.6)
plt.xlabel(r"$\gamma' a'$ (dimensionless)", fontsize=12)
plt.ylabel(r"$\rho_{90\%}/a'$", fontsize=12)
plt.title(r"Power Containment: $\rho_{90\%}/a'$ vs. $\gamma' a'$", fontsize=14)
plt.legend()
plt.tight_layout()
plt.show()

print(f"a' = {a_prime_cm}, gamma' = {gamma2}  : rho/a' = {rho2_cm}")
