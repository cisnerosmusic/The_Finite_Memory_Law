# 🌌 The Finite Memory Law (FML): A Universal Principle of Resilience

This repository hosts the complete theoretical derivation, empirical validation protocol, and reproducible code for the **Finite Memory Law (FML)**. This law posits a universal constraint governing the stability and resilience of complex dynamical systems.

The entire project is released to the **Public Domain (CC0)**. We invite the global scientific community—cosmologists, physicists, mathematicians, and systems engineers—to utilize this material for independent validation or refutation.

---

## 🌟 Core Hypothesis: The Resilience Number ($R = \tau\Omega$)

The FML suggests that dynamical systems with internal memory ($\tau$) and characteristic oscillation ($\Omega$) achieve **maximum resilience (minimum variance)** when their dimensionless product, the **Resilience Number ($R$)**, falls within a narrow range:

$$
R = \tau\Omega \in [R_{\min}, R_{\max}] \approx [0.5, 3.5]
$$

The optimal state of stability is hypothesized to occur around $R_{\text{optimal}} \approx 2.0$.

### **Key Parameters**

| Parameter | Definition | Physical Role |
| :--- | :--- | :--- |
| $\mathbf{\tau}$ | **Correlation Time** (System Memory) | The time over which the system remembers past inputs (e.g., decay time of autocorrelation). |
| $\mathbf{\Omega}$ | **Characteristic Frequency** | The dominant rate of oscillation or system response (e.g., spectral peak frequency). |
| $\mathbf{R}$ | **Resilience Number** ($\tau\Omega$) | A measure of optimal tuning between memory and oscillatory response. |

---

## 📚 Repository Contents and Documents

| File/Directory | Description | Relevance |
| :--- | :--- | :--- |
| **`The Finite Memory Law Version 2.1 - Protocol.pdf`** | **The main document.** Details the operational definitions, the strict criteria for falsifiability, the multi-domain validation strategy (ML, Climate, Fluids, Neuro), and the methodology. | **Start Here.** Defines how to test the FML. |
| **`Del Espacio de Hilbert a la Cosmología Estocástica.pdf`** | The full theoretical paper. Derives the FML from first principles using a two-field cosmological model with **self-consistent Ornstein-Uhlenbeck noise** tied to the Gibbons-Hawking temperature. | Theoretical Foundation. |
| **`Apéndice.pdf`** | Supplementary material, detailed mathematical derivations (Krein space, Fokker-Planck analysis), and technical specifications for the simulation. | Technical Deep Dive. |
| **`code/`** | **Reproducible Code.** Contains the Python script to run the canonical stochastic simulation and demonstrate the existence of the minimal variance region $R \approx 2$. | Reproducibility. |
| **`LICENSE`** | The **CC0 1.0 Universal Public Domain Dedication**. | Legal Clarity. |

---

## 🔬 How to Validate (Call for Action)

The greatest need for this project is rigorous empirical testing across diverse disciplines. We encourage researchers to:

1.  **Reproduce the Derivation:** Verify the mathematical necessity of the FML from the stochastic cosmological model (see `Del Espacio de Hilbert...pdf`).
2.  **Execute the Code:** Run the simulation in the `code/` directory to numerically confirm the minimal variance region around $R \approx 2$.
3.  **Perform Multi-Domain Tests:** Apply the operational definitions of $\tau$ and $\Omega$ (detailed in the **Protocol**) to observational data in their respective fields (e.g., **Hydrology, Economics, Neuroscience**) and test if the most stable or optimal configurations consistently yield $R \in [0.5, 3.5]$.

### **Example: Running the Simulation**

To confirm the theoretical prediction, clone this repository and run the canonical simulation:

```bash
# Clone the repository
git clone [REPLACE WITH YOUR GITHUB REPO LINK]
cd [REPO-NAME]/code/

# Ensure dependencies (numpy and scipy) are installed
# pip install numpy scipy

# Run the simulation script
python wz_demo.py
