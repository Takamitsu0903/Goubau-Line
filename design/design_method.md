# Goubau Line Design Method

---

This document summarizes the design approach for simulating and analyzing surface waves on Goubau lines. It includes the reasoning behind parameter choices and assumptions used throughout the Python scripts and HFSS models.
The majority of the design method is based on the G.Goubau's paper about the "Surface Waves and Their Application to Transmission Lines", but has sligtmodification on the method of calculation based on the recent discoveries.
## 1. Objective

- Simulate propagation modes on Goubau lines
- Understand the optimization of the launch of the surface wave
- Understand power containment and attenuation behavior
- Reproduce and extend Goubau's 1950 results with modern tools
---

## 2. Key Parameters & Justification
### Physical Parameter

| Parameter        | Symbol       | Example Value | Reasoning |
|------------------|--------------|----------------|------------|
| Dielectric const | $\varepsilon_i$ | 2.25 – 4.0     | Realistic for PTFE, polyethylene |
| Inner radius     | $a$           | 0.94 cm        | Based on commercial rods |
| Outer radius     | $a'$          | 1.0 cm         | 1 mm dielectric layer |
| Frequency        | $f$           | 3 GHz (λ = 10 cm) | Mid-microwave range |

### Mathematical Parameter

- Propagation constant-guided wave( $h$ ):  
- Propagation constant-free space wave( $k$ ): 
- Power confined outiside of raidus ( $N_{\rho}$ ): total power of the wave which travels
outside of a cylinder of radius p surrounding the wire. ie. $\infty > r > $\rho$
- Layer scaling factor($G$): G is propotional function with the ratio of a' and a
- Power distribution function ($F(\gamma' \rho)$): F is a propotional function that shows how much power is outside of the radius $\rho$   

---

## 3. Calculation Steps

1. Compute $G(\gamma' a')$ from geometry (a', a, $\epsilon_r$, and frequency)
2. Solve for $\gamma' a'$ numerically
3. Plot power confinement ($\rho$/a'), and use that to find the $\rho$ - minimum aperture size.
---

## 4. Notes on Assumptions

- Use TM01-like mode only
- Perfect conductor assumed unless otherwise stated.
- Quasi-static approximation valid for small $\gamma' a'$

## 5. Key finding:
- The structure technically has the cutoff for the wave to propagation, but the cutoff is not only dependent on the frequency, it is also dependent on the $\lambda$, and ratio $\frac{a'}{a}$, permittivities $\epsilon_i$ and $\epsilon$. This is not directly related, but depending on the $G(\gamma'a')$ that determined there will and will not be a solution for the $\gamma'a'$.
- 
