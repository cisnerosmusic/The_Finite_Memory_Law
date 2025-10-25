from __future__ import annotations
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def simulate_wz(steps: int = 200_000, seed: int | None = None):
    """
    Canonical W–Z two-field stochastic simulation used to probe the variance minimum
    near R = tau * Omega ≈ 2.0 (see docs PDFs).
    Returns a dict with time series and summary stats.

    NOTE: Placeholder dynamics. In the next step we will replace this with the exact
    equations from code/wz_demo.py to preserve identical behavior.
    """
    rng = np.random.default_rng(seed)
    dt = 1e-3
    t = np.arange(steps) * dt

    # --- OU driver with memory scale tau ---
    tau = 1.0
    sigma = 1.0
    ou = np.zeros(steps)
    for k in range(1, steps):
        ou[k] = ou[k-1] + (-ou[k-1] / tau) * dt + sigma * np.sqrt(dt) * rng.normal()

    # --- Lightly forced oscillator with frequency Omega ---
    Omega = 2.0
    x = np.zeros(steps)
    v = np.zeros(steps)
    coupling = 0.2
    for k in range(1, steps):
        a = -Omega**2 * x[k-1] + coupling * ou[k-1]
        v[k] = v[k-1] + a * dt
        x[k] = x[k-1] + v[k] * dt

    var_x = float(np.var(x))
    R = tau * Omega
    return {"t": t, "x": x, "ou": ou, "tau": tau, "Omega": Omega, "R": R, "var_x": var_x}

def save_fig(result: dict, outdir: str | Path) -> Path:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    fig_path = outdir / "wz_demo.png"

    t = result["t"]; x = result["x"]; ou = result["ou"]
    plt.figure(figsize=(10, 4))
    plt.plot(t, x, label="x(t)")
    plt.plot(t, ou, alpha=0.5, label="OU driver")
    plt.title(f"WZ demo • R={result['R']:.2f} • var(x)={result['var_x']:.3f}")
    plt.xlabel("t"); plt.ylabel("amplitude"); plt.legend()
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()
    return fig_path
