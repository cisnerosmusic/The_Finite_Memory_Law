from __future__ import annotations
import argparse
from pathlib import Path
from .sim import simulate_wz, save_fig

def main():
    p = argparse.ArgumentParser(description="Finite Memory Law — WZ simulation")
    p.add_argument("--steps", type=int, default=200_000, help="simulation steps")
    p.add_argument("--seed", type=int, default=None, help="random seed")
    p.add_argument("--save-media", type=str, default="./media", help="folder to save figures")
    args = p.parse_args()

    res = simulate_wz(steps=args.steps, seed=args.seed)
    path = save_fig(res, args.save_media)
    print(f"[FML] R={res['R']:.3f} var(x)={res['var_x']:.6f} figure={Path(path).as_posix()}")

if __name__ == "__main__":
    main()
