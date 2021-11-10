import subprocess
import random

# Automated random search experiments
num_exps = 3
random.seed(1)

for _ in range(num_exps):
    params = {
        "rand_n_est_value": random.randint(26, 208),
        "rand_min_split_value": random.randint(305, 505)
    }
    subprocess.run(["dvc", "exp", "run", "--queue",
                    "--set-param", f"train.n_est={params['rand_n_est_value']}",
                    "--set-param", f"train.min_split={params['rand_min_split_value']}"])
