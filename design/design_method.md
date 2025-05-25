# Goubau Line Design Method

This document summarizes the design approach for simulating and analyzing surface waves on Goubau lines. It includes the reasoning behind parameter choices and assumptions used throughout the Python scripts and HFSS models.

---

## 1. Objective

- Simulate propagation modes on Goubau lines
- Understand power containment and attenuation behavior
- Reproduce and extend Goubau's 1950 results with modern tools

---

## 2. Key Parameters & Justification

| Parameter        | Symbol       | Example Value | Reasoning |
|------------------|--------------|----------------|------------|
| Dielectric const | $\varepsilon_i$ | 2.25 – 4.0     | Realistic for PTFE, polyethylene |
| Inner radius     | $a$           | 0.94 cm        | Based on commercial rods |
| Outer radius     | $a'$          | 1.0 cm         | 1 mm dielectric layer |
| Frequency        | $f$           | 3 GHz (λ = 10 cm) | Mid-microwave range |

---

## 3. Calculation Steps

1. Compute $G(\gamma' a')$ from geometry
2. Solve for $\gamma' a'$ numerically
3. Plot power confinement and attenuation
4. (Optional) Validate in HFSS using equivalent mode excitation

---

## 4. Notes on Assumptions

- Use TM0-like mode only
- Perfect conductor assumed unless otherwise stated
- Quasi-static approximation valid for small $\gamma' a'$
