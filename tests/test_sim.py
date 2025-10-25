from fml.sim import simulate_wz

def test_sim_smoke():
    res = simulate_wz(steps=1000, seed=123)
    assert "R" in res and "var_x" in res
    assert res["t"].shape[0] == 1000
